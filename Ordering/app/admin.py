from django.contrib import admin
from .models import Customer, Item, Order, OrderItem, Delivery

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)