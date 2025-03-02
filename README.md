# Руководство по развёртыванию проекта

## Развёртывание проекта

### 1 Клонирование репозитория
```sh
$ git clone https://github.com/KiselevDV/test-task-django-rishat.git
$ cd test-task-django-rishat/docker
```

### 2 Запуск контейнеров
```sh
# Запуск с пересборкой контейнеров
$ docker-compose build --no-cache

# Запуск в фоновом режиме
$ docker-compose up -d
```

## Документация
Дополнительные инструкции расположены в директории `docs`:

- [Дополнительные команды](docs/commands.md)
- [Работа с API через Django](docs/api_django.md)
- [Работа с API через DRF](docs/api_drf.md)
