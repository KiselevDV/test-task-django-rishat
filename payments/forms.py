from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from payments.models import Order, Item


class OrderAdminForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=FilteredSelectMultiple('Товары', is_stacked=False),
        required=False,
        label=''
    )

    total_price = forms.CharField(
        label='Итоговая цена',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'style': 'border: none; font-weight: bold;'})
    )

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['total_price'].initial = f'{self.instance.get_total_price()}'


class ItemAdminForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'size': 80}),
        label='Название'
    )

    class Meta:
        model = Item
        fields = '__all__'
