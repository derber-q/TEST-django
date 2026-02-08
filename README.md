# TEST-django

Базовый Django-проект `test_django`.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

После запуска приложение `shopapp` доступно по адресу `http://127.0.0.1:8000/shop/`.
