import os
from pathlib import Path
from typing import Dict, Literal, List

# Настройки путей
BASE_DIR = Path(__file__).parent.parent
DB_DIR = BASE_DIR / "data"
DB_DIR.mkdir(exist_ok=True)

# Пути к файлам данных
CHAT_HISTORY_PATH = DB_DIR / "chat_history.json"
USER_SETTINGS_PATH = DB_DIR / "user_settings.json"

# Голосовые параметры
VOICE_CONFIG: Dict[str, Dict[str, str]] = {
    "male": {
        "en": "com",    # Английский мужской (американский)
        "fr": "ca",     # Французский мужской (канадский)
        "es": "com.mx", # Испанский мужской (мексиканский)
        "de": "de"      # Немецкий мужской
    },
    "female": {
        "en": "co.uk",  # Английский женский (британский)
        "fr": "fr",     # Французский женский (французский)
        "es": "es",     # Испанский женский (испанский)
        "de": "de"      # Немецкий женский
    }
}

# Настройки голосов
VOICE_SETTINGS = {
    "ru": {"gender": ["female", "male"], "accent": "russia"},
    "en": {"gender": ["female", "male"], "accent": ["us", "uk"]},
    "es": {"gender": ["female", "male"], "accent": ["spain", "mexico"]},
    "it": {"gender": ["female", "male"], "accent": "italia"},
    "ja": {"gender": ["female", "male"], "accent": "japan"},
    # ... другие языки
}

VOICE_REFERENCES = {
    "es": {"region": "eu"},  # Испанский (европейский)
    "ru": {"region": None}   # Русский без региона
}

VOICE_SETTINGS.update({
    "it": {"tld": "it", "speed": 1.05, "lang": "it"},
    "ja": {"tld": "co.jp", "speed": 0.95, "lang": "ja"},
    "zh": {"tld": "com", "speed": 0.9, "lang": "zh-CN"}
})

# Настройки форматирования ответов
RESPONSE_FORMAT = {
    "section_headers": {
        "target": "### 1. Основной ответ ({language})",
        "translation": "### 2. Дословный перевод ({native_lang})",
        "analysis": "### 3. Разбор фраз",
        "advanced": "### 4. Дополнительно"
    },
    "markers": {
        "keywords": "➤",
        "mistakes": "⚠️",
        "culture": "🌍",
        "nuances": "💡",
        "alternatives": "🔍"
    }
}

# Полный шаблон промпта для языкового ментора
MENTOR_PROMPT_TEMPLATE = """
Ты — профессиональный AI-преподаватель языков. Всегда строго следуй этому формату:

### 1. Основной ответ (изучаемый язык: {target_language})
[Полный ответ только на целевом языке. Без пояснений!]

### 2. Дословный перевод (родной язык: {native_language})
[Точный перевод без изменений. Без интерпретаций!]

### 3. Разбор фраз (для уровней A1-B2)
- ➤ **Ключевые слова**:
  [Слово/фраза 1] - [перевод] (пример: "[пример на целевом языке] → [перевод]")
  [Слово/фраза 2] - [перевод] (контекст: "[употребление в речи]")
- ⚠️ **Типичные ошибки**:
  [Неправильно] → [Правильно] (объяснение: "Почему?")
- 🌍 **Культурный контекст**:
  [Интересный факт или норма поведения]

### 4. Дополнительно (для уровней C1-C2)
- 💡 **Нюансы языка**:
  [Стилистические/диалектные особенности]
- 🔍 **Альтернативные варианты**:
  [Синонимичные фразы с разной стилистикой]

---

### Жесткие правила:
1. **Разделение языков**:
   - Никогда не смешивай языки в одном предложении
   - Скобки () используй ТОЛЬКО для примеров/пояснений в разделе 3

2. **Адаптация под уровень**:
   - A1-A2: Максимально простые фразы + 2-3 разбора
   - B1-B2: Естественные конструкции + 1-2 нюанса
   - C1-C2: Акцент на идиомах и стилистике

3. **Форматирование**:
   - Обязательные маркеры (###, ➤, ⚠️, 🌍)
   - Пустые строки между разделами
   - Кавычки «» для примеров

---

### Пример ответа (французский, уровень A2):
### 1. Основной ответ (французский)
Bonjour, je voudrais réserver une table pour deux personnes, s'il vous plaît.

### 2. Дословный перевод (русский)
Здравствуйте, я хотел бы зарезервировать столик на двоих, пожалуйста.

### 3. Разбор фраз
- ➤ **Ключевые слова**:
  «je voudrais» - «я хотел бы» (пример: «Je voudrais un café» → «Я хотел бы кофе»)
  «une table» - «столик» (контекст: «резервация в ресторане»)
- ⚠️ **Типичные ошибки**:
  «Je veux» → «Je voudrais» (объяснение: "Je veux звучит грубо в этом контексте")
- 🌍 **Культурный контекст**:
  Во Франции принято называть точное время брони («pour 19h»)

### 4. Дополнительно (для B2+)
- 💡 **Нюансы языка**:
  В неформальной обстановке можно сказать «Je vais prendre...» (досл. «Я возьму...»)
- 🔍 **Альтернативные варианты**:
  Официально: «Je souhaiterais...» (более вежливо)
  Друзьям: «On peut avoir...?» («Можно нам...?»)
"""

# Настройки генеративного AI
GEMINI_CONFIG = {
    "model_name": "gemini-1.5-pro-latest",
    "safety_settings": [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }
    ],
    "generation_config": {
        "temperature": 0.7,
        "top_p": 0.9,
        "max_output_tokens": 2000,
        "stop_sequences": ["###"]  # Чтобы избежать бесконечных ответов
    }
}

# Уровни сложности
LEVEL_DESCRIPTIONS = {
    "A1": "Начинающий (понимает простые фразы)",
    "A2": "Элементарный (может общаться на бытовые темы)",
    "B1": "Средний (может поддерживать беседу)",
    "B2": "Выше среднего (свободно говорит на большинство тем)",
    "C1": "Продвинутый (понимает сложные тексты)",
    "C2": "Владение в совершенстве"
}

# Настройки для автонапоминаний
REMINDER_SETTINGS = {
    "min_interval_hours": 24,
    "max_interval_hours": 48,
    "reminder_messages": {
        "en": [
            "Hey! Let's practice some {language} today!",
            "Ready for our daily {language} chat?"
        ],
        "ru": [
            "Привет! Давай сегодня попрактикуем {language}!",
            "Готов к нашей ежедневной практике {language}?"
        ]
    }
}

# Добавьте в конец файла:

# Настройки TTS
TTS_CONFIG = {
    "model": "xtts_v2",
    "languages": {
        "en": {"speakers": ["male", "female"], "accents": ["us", "uk"]},
        "ru": {"speakers": ["male", "female"], "accents": ["russia"]},
        # ... другие языки
    },
    "default_speaker": "female",
    "silence_duration_ms": 800
}

# Лимиты для безопасности
SAFETY_LIMITS = {
    "max_text_length": 1000,
    "min_interval_seconds": 5
}

# Настройки кэширования
CACHE_SETTINGS = {
    "voice_cache_ttl": 3600,  # 1 час
    "max_cache_size": 100  # Макс. количество файлов
}

# В конец файла добавьте:
DEFAULT_SETTINGS = {
    "max_response_length": 500,
    "auto_reminders": True,
    "speech_speed": 1.0,
    "feedback_level": "detailed"  # basic/normal/detailed
}

# Настройки референсных голосов
VOICE_REFERENCE_FORMATS = {
    # Языки с акцентами
    "es": "{lang}_{region}_{gender}.wav",  # es_eu_female.wav, es_la_male.wav
    "en": "{lang}_{region}_{gender}.wav",  # en_uk_female.wav, en_us_male.wav

    # Языки без акцентов
    "ru": "{lang}_{gender}.wav",  # ru_female.wav
    "ja": "{lang}_{gender}.wav",
    "zh": "{lang}_{gender}.wav"
}

# Регионы по умолчанию для языков с акцентами
DEFAULT_REGIONS = {
    "es": "eu",  # Испанский (европейский)
    "en": "us"  # Английский (американский)
}
