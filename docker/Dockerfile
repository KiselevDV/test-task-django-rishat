FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY ../pyproject.toml ../poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi --no-root

COPY ../ /app/

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

# CMD python ./manage.py runserver 0.0.0.0:8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]