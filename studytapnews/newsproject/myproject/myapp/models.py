# models.py

from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('placed', 'Order Placed'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} - {self.product_name}"
