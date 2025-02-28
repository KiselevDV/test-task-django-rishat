# Руководство по развёртыванию проекта

## 1. Развёртывание проекта

### 1.1 Клонирование репозитория
```sh
$ git clone https://github.com/KiselevDV/test-task-django-rishat.git
$ cd test-task-django-rishat/docker
```

### 1.2 Запуск контейнеров
```sh
# Запуск с пересборкой контейнеров
$ docker-compose up --build

# Запуск в фоновом режиме
$ docker-compose up -d
```

## 2. Дополнительные команды

### 2.1 Заполнение базы данных фикстурами
```sh
# Вход в контейнер с Django
$ docker-compose exec web bash

# Запуск скрипта инициализации БД
$ python init_db.py
```

### 2.2 Доступ к админ-панели Django
Админ-панель доступна по адресу: [http://127.0.0.1:18000/admin/](http://127.0.0.1:18000/admin/)

**Данные для входа:**
```
Логин: admin
Пароль: admin123
```

### 2.3 Линтинг кода
```sh
$ docker-compose exec web flake8
```

## 3. Работа с API через Django

### 3.1 `create_payment_intent`
Создаёт платежное намерение для заказа и возвращает `client_secret` для завершения платежа через Stripe.

**Эндпоинт:**
```
POST /payments/payment-order/<order_id>/
```
**Параметры:**
- `order_id` (int) — ID заказа, который необходимо оплатить.

**Ответ:**
```json
{
    "client_secret": "some_secret_key"
}
```

### 3.2 `payment_success`
Страница успешного платежа.

**Эндпоинт:**
```
GET /payments/success/
```
**Ответ:** HTML-страница с подтверждением успешного платежа.

### 3.3 `payment_error`
Страница ошибки платежа.

**Эндпоинт:**
```
GET /payments/error/
```
**Ответ:** HTML-страница с сообщением об ошибке платежа.

## 4. Альтернативная работа с API, через DRF (с возможностью дальнейшего расширения)

### 4.1 Создание платежного намерения (create_payment_intent)
**Описание:** Создаёт платежное намерение для заказа.

**Метод:** `POST`

**URL:** `/api/payment-order/{order_id}/`

**Пример запроса:**
```sh
curl -X POST http://127.0.0.1:18000/api/payment-order/1/
```

**Ответ:**
```json
{
    "client_secret": "pi_1234567890abcdef"
}
```

### 4.2 Получение списка товаров (ItemListView)
**Метод:** `GET`

**URL:** `/api/items/`

**Пример запроса:**
```sh
curl -X GET http://127.0.0.1:18000/api/items/
```

**Ответ:**
```json
[
    {
        "id": 1,
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": "100.00",
        "currency": "USD"
    },
    ...
]
```

### 4.3 Получение информации о товаре (ItemDetailView)
**Метод:** `GET`

**URL:** `/api/items/{id}/`

**Пример запроса:**
```sh
curl -X GET http://127.0.0.1:18000/api/items/1/
```

**Ответ:**
```json
{
    "id": 1,
    "name": "Товар 1",
    "description": "Описание товара 1",
    "price": "100.00",
    "currency": "USD"
}
```

### 4.4 Получение списка заказов (OrderListView)
**Метод:** `GET`

**URL:** `/api/orders/`

**Пример запроса:**
```sh
curl -X GET http://127.0.0.1:18000/api/orders/
```

**Ответ:**
```json
[
    {
        "id": 1,
        "items": [...],
        "created_at": "2024-02-28T12:34:56Z"
    },
    ...
]
```

### 4.5 Получение информации о заказе (OrderDetailView)
**Метод:** `GET`

**URL:** `/api/orders/{id}/`

**Пример запроса:**
```sh
curl -X GET http://127.0.0.1:18000/api/orders/1/
```

**Ответ:**
```json
{
    "id": 1,
    "items": [...],
    "created_at": "2024-02-28T12:34:56Z"
}
```