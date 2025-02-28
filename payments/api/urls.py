from django.urls import path

from payments.api.views import (
    CreatePaymentIntentView, ItemListView, ItemDetailView, OrderListView, OrderDetailView)

app_name = 'api'

urlpatterns = [
    path('payment-order/<int:order_id>/', CreatePaymentIntentView.as_view(), name='create_payment_intent'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
