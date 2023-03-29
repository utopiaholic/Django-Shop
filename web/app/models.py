from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name}'s {self.item_name} x{self.quantity}"
