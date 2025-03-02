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

[Вернутся на главную](../README.md)