release: python manage.py migrate && python manage.py loaddata fixtures/seed.json
web: gunicorn blog_platform.wsgi