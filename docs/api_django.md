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

[Вернутся на главную](../README.md)