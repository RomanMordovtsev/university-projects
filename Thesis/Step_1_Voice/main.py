import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from core.models import UserSettings, ChatRequest
from core.history_manager import DatabaseManager
from core.voice_handler import VoiceHandler
from core.config import MENTOR_PROMPT_TEMPLATE, GEMINI_CONFIG, LEVEL_DESCRIPTIONS
from typing import Dict, Any, Optional

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Language Mentor API",
    description="AI Language Learning Assistant with Voice Support",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()
voice = VoiceHandler()

try:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("Gemini API key not found in .env file")

    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel(
        model_name=GEMINI_CONFIG["model_name"],
        generation_config=genai.types.GenerationConfig(
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            max_output_tokens=2000
        ),
        safety_settings=GEMINI_CONFIG["safety_settings"]
    )
    logger.info("Gemini model initialized successfully")
except Exception as e:
    logger.critical(f"Gemini initialization failed: {e}")
    raise RuntimeError("Failed to initialize Gemini API") from e

@app.post("/setup")
async def setup_user(settings: UserSettings) -> Dict[str, Any]:
    try:
        if not settings.target_languages:
            raise HTTPException(status_code=400, detail="At least one target language required")

        db.save_settings(settings)
        return {
            "message": f"Settings saved for user {settings.user_id}",
            "languages": settings.target_languages,
            "level": LEVEL_DESCRIPTIONS.get(settings.level, "Unknown level")
        }
    except Exception as e:
        logger.error(f"Setup error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest) -> Dict[str, Any]:
    try:
        settings_data = db.get_settings(request.user_id)
        if not settings_data:
            default_settings = UserSettings(user_id=request.user_id, target_languages=["en"]).dict()
            db.save_settings(UserSettings(**default_settings))
            settings_data = default_settings

        settings = UserSettings(**settings_data)
        target_lang = settings.target_languages[0]
        native_lang = settings.native_language
        gender = settings.voice_gender or "female"
        region = request.voice_region or settings.voice_region

        history = db.get_history(request.user_id)
        history_text = "\n".join([f"{msg['sender']}: {msg['message']}" for msg in history])

        prompt = MENTOR_PROMPT_TEMPLATE.format(
            target_language=target_lang,
            native_language=native_lang
        )
        full_input = f"{prompt}\n\nИстория:\n{history_text}\n\nПользователь: {request.message}"

        # Получаем ответ от модели
        try:
            response = gemini_model.generate_content(full_input)
            if not response.text:
                raise ValueError("Empty response from model")
            response_text = response.text.strip()
        except Exception as e:
            logger.error(f"Model generation failed: {e}")
            response_text = "Sorry, I couldn't generate a response. Please try again."

        # Сохраняем сообщения в историю
        db.save_message(request.user_id, request.message, sender="user")
        db.save_message(request.user_id, response_text, sender="bot")

        voice_success = False
        if request.is_voice and response_text:  # Добавлена проверка на наличие response_text
            try:
                voice_success = voice.speak_response(
                    text=response_text,
                    target_lang=target_lang,
                    native_lang=native_lang,
                    gender=gender,
                    region=region
                )
            except Exception as e:
                logger.error(f"Voice processing failed: {e}")

        return {
            "response": response_text,
            "language": target_lang,
            "voice_processed": request.is_voice and voice_success
        }
    except Exception as e:
        logger.exception("Chat error")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
