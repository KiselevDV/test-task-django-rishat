FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi --no-root

RUN poetry run pip install flake8

COPY . /app/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]