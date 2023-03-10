from django.db import models
from accounts.models import Account
from store.models import Product
from carts.models import Variation

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=128)
    payment_method = models.CharField(max_length=128)
    amount_paid = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=32)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=128)
    adress_line_1 = models.CharField(max_length=128)
    adress_line_2 = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    order_note = models.TextField(max_length=128, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=128, choices=STATUS, default='New')
    ip = models.CharField(max_length=128, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
    def full_adress(self):
        return f'{self.adress_line_1} {self.adress_line_2}'
    
    
    def __str__(self):
        name = self.user.first_name
        return name


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation, blank=True)
    color = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.product_name