from django.urls import path, include

from payments.views import buy_item, item_page, create_payment_intent, payment_success, payment_error

app_name = 'payments'

urlpatterns = [
    path('api/', include('payments.api.urls')),
    # path('buy/<int:item_id>/', buy_item, name='buy_item'),
    # path('item/<int:item_id>/', item_page, name='item_page'),
    path('payment-order/<int:order_id>/', create_payment_intent, name='create_payment_intent'),
    path('success/', payment_success, name='payment_success'),
    path('error/', payment_error, name='payment_error'),
]
