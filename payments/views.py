import stripe

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings

from payments.models import Item, Order


def buy_item(request, item_id):
    """Оплата товара через Checkout Session"""
    item = get_object_or_404(Item, id=item_id)

    # Выбрать ключ в зависимости от валюты
    stripe_keys = settings.STRIPE_KEYS.get(item.currency, settings.STRIPE_KEYS['USD'])
    stripe.api_key = stripe_keys['secret']

    amount_in_cents = int(item.price * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': amount_in_cents,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': session.id})


def item_page(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    # Выбрать ключ в зависимости от валюты
    stripe_keys = settings.STRIPE_KEYS.get(item.currency, settings.STRIPE_KEYS['usd'])
    return render(request, 'items.html', {'item': item, 'stripe_public_key': stripe_keys['public']})


def create_payment_intent(request, order_id):
    """Оплата заказа через Payment Intent"""
    order = get_object_or_404(Order, id=order_id)
    print('order - ', order.get_total_price())

    # Выбрать ключ в зависимости от валюты
    first_item = order.items.first()
    currency = first_item.currency if first_item else 'USD'
    stripe_keys = settings.STRIPE_KEYS.get(currency, settings.STRIPE_KEYS['USD'])
    stripe.api_key = stripe_keys['secret']

    amount_in_cents = int(order.get_total_price() * 100)  # общая сумма заказа

    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency=currency,
            payment_method_types=['card'],
        )
        order.stripe_payment_id = intent.id
        order.save()
        return JsonResponse({'client_secret': intent.client_secret})

    return render(
        request, 'orders.html',
        {'order': order, 'stripe_public_key': stripe_keys['public']}
    )


def payment_success(request):
    return render(request, 'payment_success.html')


def payment_error(request):
    return render(request, 'payment_error.html')
