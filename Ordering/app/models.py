from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, default='Mineral water gallon')
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivery', 'Delivery'),
        ('Customer Pick-up', 'Customer Pick-up'),
    ]
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivered_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
