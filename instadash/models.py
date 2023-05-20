from django.db import models
from django.core.validators import RegexValidator
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

class Cart(models.Model):
    orders = models.ManyToManyField(User, through="OrderHistory")

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

class Business(models.Model):
    class expensive(models.TextChoices):
        cheap = '$'
        budget = '$$'
        expensive = '$$$'

    name = models.CharField(max_length=200)
    rating_score = models.DecimalField(max_digits=2, decimal_places=1)
    open_time = models.TimeField()
    close_time = models.TimeField()
    expensive_rating = models.CharField(choices=expensive.choices)


class Item(models.Model):
    name = models.CharField(max_length=200)
    prices = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, null=True)
    carts = models.ManyToManyField(Cart)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    
