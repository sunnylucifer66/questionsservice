<h1 align="center">Привет! Я <a href="https://github.com/sunnylucifer66" target="_blank">Дима</a>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Python разработчик из России 🇷🇺</h3>

# Это вопросный сервис с генерацией советов

Этот проект представляет собой веб-сервис для генерации персонализированных советов с использованием FastAPI и OpenAI API (или GPT-4). Пользователи могут регистрироваться, входить в систему, задавать вопросы и получать советы, основанные на их интересах и целях.

## Стек технологий

- **FastAPI** — веб-фреймворк для Python для создания API.
- **SQLAlchemy** — ORM для взаимодействия с базой данных.
- **Passlib** — библиотека для безопасного хеширования паролей.
- **SQLite** — база данных для хранения информации о пользователях и запросах.(В будущем заменю)
- **OpenAI API (GPT-4)** — для генерации советов на основе запросов пользователей.

## Описание

1. **Регистрация пользователя**: Пользователь может зарегистрироваться, указав свой email, пароль, имя, возраст, интересы и цели.
2. **Авторизация пользователя**: Пользователь может войти в систему, используя свою электронную почту и пароль.
3. **Генерация совета**: Пользователь может задать вопрос, и система на основе его интересов и целей предоставит персонализированный совет.
4. **История запросов**: Пользователь может просматривать историю своих запросов и советов, которые были ему предоставлены.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. Установите зависимости:
   -pip install -r req.txt

3. Запустите приложение:
   -uvicorn app.main:app --reload

## Устранение неполадок: если метод generate_advice не работает

Если метод generate_advice не работает корректно, выполните следующие шаги для решения проблемы:

Обновите зависимости: Убедитесь, что ваш проект использует последнюю версию необходимых библиотек. Для этого следуйте инструкциям по установке и обновлению зависимостей, указанным в разделе Getting Started репозитория.

Обновите Pydantic: Проверьте, что у вас установлена последняя версия Pydantic. Иногда проблемы могут возникать из-за устаревших версий библиотек, поэтому обновление до последней стабильной версии Pydantic может помочь решить возможные проблемы с совместимостью.


