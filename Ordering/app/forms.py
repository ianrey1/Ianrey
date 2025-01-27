from django import forms
from .models import Customer, Item, Order, OrderItem, Delivery

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'age', 'address', 'phone']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['price', 'stock']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivered_by']
