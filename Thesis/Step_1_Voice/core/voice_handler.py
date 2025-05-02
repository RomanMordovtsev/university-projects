import os
import tempfile
from pathlib import Path
from typing import Optional
import logging
from datetime import datetime
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
import re
from .config import VOICE_REFERENCE_FORMATS, DEFAULT_REGIONS

logger = logging.getLogger(__name__)


class VoiceHandler:
    def __init__(self):
        # Создаем собственную временную директорию
        self.temp_dir = Path("C:/mentor_audio_temp")
        self.temp_dir.mkdir(exist_ok=True, mode=0o777)

        self.reference_dir = Path("reference_speakers_wav")
        self.reference_dir.mkdir(exist_ok=True)

        try:
            self.tts = TTS(
                model_name="tts_models/multilingual/multi-dataset/xtts_v2",
                progress_bar=False,
                gpu=False
            )
            logger.info("XTTS v2 model initialized")
        except Exception as e:
            logger.critical(f"TTS init failed: {e}")
            raise

    def speak_response(self, text: str, target_lang: str, native_lang: str,
                       gender: str = "female", region: Optional[str] = None) -> bool:
        try:
            if not isinstance(text, str) or not text.strip():
                logger.warning("Invalid or empty text received")
                return False

            target_text = self._extract_section(text, "Основной ответ") or ""
            native_text = self._extract_section(text, "Дословный перевод") or ""

            if target_text:
                self._play_audio(target_text, target_lang, gender, region)
                sd.sleep(800)  # Пауза между фразами

            if native_text:
                self._play_audio(native_text, native_lang, gender, region)

            return True
        except Exception as e:
            logger.error(f"Speech synthesis failed: {e}", exc_info=True)
            return False

    def _play_audio(self, text: str, lang: str, gender: str, region: Optional[str]):
        """Новый метод воспроизведения без временных файлов"""
        try:
            ref_path = self._get_reference_path(lang, gender, region)
            if not ref_path.exists():
                raise FileNotFoundError(f"Missing reference voice: {ref_path.name}")

            # Вариант 1: Воспроизведение через sounddevice (в памяти)
            with tempfile.NamedTemporaryFile(suffix='.wav', dir=str(self.temp_dir)) as tmp_file:
                self.tts.tts_to_file(
                    text=text,
                    speaker_wav=str(ref_path),
                    language=lang,
                    file_path=tmp_file.name,
                    split_sentences=True
                )
                data, samplerate = sf.read(tmp_file.name)
                sd.play(data, samplerate)
                sd.wait()

        except Exception as e:
            logger.error(f"Primary playback failed, trying fallback: {e}")
            # Вариант 2: Через ffplay (если sounddevice не работает)
            self._fallback_play(text, lang, ref_path)

    def _fallback_play(self, text: str, lang: str, ref_path: Path):
        """Резервный метод воспроизведения"""
        temp_path = self.temp_dir / f"temp_{datetime.now().timestamp()}.wav"
        try:
            self.tts.tts_to_file(
                text=text,
                speaker_wav=str(ref_path),
                language=lang,
                file_path=str(temp_path),
                split_sentences=True
            )
            import subprocess
            subprocess.run(['ffplay', '-nodisp', '-autoexit', str(temp_path)], check=True)
        finally:
            if temp_path.exists():
                try:
                    temp_path.unlink()
                except:
                    pass

    def _get_reference_path(self, lang: str, gender: str, region: Optional[str] = None) -> Path:
        fmt = VOICE_REFERENCE_FORMATS.get(lang, "{lang}_{gender}.wav")
        region = region or DEFAULT_REGIONS.get(lang)
        filename = fmt.format(lang=lang, gender=gender, region=region)
        return self.reference_dir / filename

    def _extract_section(self, text: str, section_title: str) -> Optional[str]:
        if not isinstance(text, str) or not text.strip():
            return None

        try:
            pattern = rf"### \d+\. {re.escape(section_title)}.*?\n(.*?)(?=###|\Z)"
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            return match.group(1).strip() if match else None
        except Exception:
            return None