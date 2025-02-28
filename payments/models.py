from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Доллары США'),
        ('EUR', 'Евро'),
        ('RUB', 'Рубли'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Цена', help_text='Укажите цену в валюте товара')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB', verbose_name='Валюта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} ({self.currency.upper()})'


class Discount(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Размер скидки',
        help_text='Указать сумму скидки в валюте заказа')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.name} (-{self.amount})'


class Tax(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Процент налога',
        help_text='Процент, который будет добавлен к стоимости заказа')

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders', verbose_name='Товары')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Скидка')
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Налог')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления заказа')
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='ID платежа в Stripe')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} от {self.created_at.strftime('%Y-%m-%d %H:%M')}'

    def get_total_price(self):
        """Общая стоимость заказа с учетом скидки и налога"""
        total = sum(item.price for item in self.items.all())

        if self.discount:
            total -= self.discount.amount

        if self.tax:
            tax_amount = total * (self.tax.percentage / 100)
            total += tax_amount

        return max(round(total, 2), 0)
