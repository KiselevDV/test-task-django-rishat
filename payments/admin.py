from django.contrib import admin
from payments.models import Item, Discount, Tax, Order
from payments.forms import OrderAdminForm, ItemAdminForm


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ('name', 'price', 'currency')
    search_fields = ('name', 'description')
    list_filter = ('currency',)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')
    search_fields = ('name',)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('id', 'created_at', 'stripe_payment_id', 'get_total_price_display')
    search_fields = ('id', 'stripe_payment_id')
    list_filter = ('created_at',)
    autocomplete_fields = ('discount', 'tax')
    filter_horizontal = ('items',)

    def get_total_price_display(self, obj):
        return f'{obj.get_total_price()}' if obj.items.exists() else '0'

    get_total_price_display.short_description = 'Итоговая цена'
