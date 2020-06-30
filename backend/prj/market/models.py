from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    adress = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'


class Category(models.Model):
    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.name,self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Store(models.Model):
    provider =models.ForeignKey(Provider, on_delete=models.CASCADE)
    prodict =models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class Order(models.Model):

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='new', choices=STATUS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    ammount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
