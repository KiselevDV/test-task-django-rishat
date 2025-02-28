import stripe

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from payments.api.serializers import ItemSerializer, OrderSerializer
from payments.models import Order, Item


class CreatePaymentIntentView(APIView):
    """Создание Payment Intent для заказа"""
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        first_item = order.items.first()
        currency = first_item.currency if first_item else 'USD'
        stripe_keys = settings.STRIPE_KEYS.get(currency, settings.STRIPE_KEYS['USD'])
        stripe.api_key = stripe_keys['secret']

        amount_in_cents = int(order.get_total_price() * 100)
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency=currency,
                payment_method_types=['card'],
            )
            order.stripe_payment_id = intent.id
            order.save()
            return Response({'client_secret': intent.client_secret}, status=status.HTTP_201_CREATED)
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
