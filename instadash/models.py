from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    # def get_full_name(self):
    #     return self.first_name, self.last_name

    # def get_short_name(self):
    #     return self.first_name

    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=17, blank=True)

class Business(models.Model):
    class expensive(models.TextChoices):
        cheap = '$'
        budget = '$$'
        expensive = '$$$'
    category_choices = (('convenience', 'Convenience'),  ('grocery', 'Grocery'), (
        'alcohol', 'Alcohol'), ('pets', 'Pets'), ('flowers', 'Flowers'), ('shipping', 'Shipping'), ('packages', 'Packages'), ('gifts', 'Gifts'))
    food_type_choices = (('fast_food', 'Fast Food'), ('mexican', 'Mexican'), ('desserts', 'Desserts'), ('chicken', 'Chicken'), ('burgers', 'Burgers'),
                         ('soup', 'Soup'), ('snack', 'Snack'), ('pizza', 'Pizza'), ('drinks', 'Drinks'), ('chinese', 'Chinese'), ('sandwiches',
                         'Sandwiches'), ('smoothie', 'Smoothie'), ('coffee', 'Coffee'), ('healthy', 'Healthy'), ('breakfast', 'Breakfast'), ('salad', 'Salad'),
                         ('italian', 'Italian'), ('seafood', 'Seafood'), ('barbeque', 'Barbeque'), ('bakery', 'Bakery'), ('asian', 'Asian'), ('thai', 'Thai'))
    dashboard_choices = (('national', 'National Favorties'), ('breakfast', 'Best of Breakfast'), (
        'lunch', 'Best of Lumch'), ('convenience', 'Convenience & Drugstores'), ('grocery', 'Grocery'))
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='files/business', null=True)
    category = MultiSelectField(
        choices=category_choices, blank=True, max_length=255)
    food_type = MultiSelectField(
        choices=food_type_choices, blank=True, max_length=255)
    dashboard = MultiSelectField(
        choices=dashboard_choices, blank=True, max_length=255)
    favorite = models.BooleanField(default=False)
    rating_score = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)
    ratings = models.IntegerField(blank=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    expensive_rating = models.CharField(choices=expensive.choices)


class Item(models.Model):
    name = models.CharField(max_length=200)
    prices = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, null=True)
    # products = models.ManyToManyField(Cart, through="ItemCart")
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/item', null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    isCart = models.BooleanField(default=True)


class Ad(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True)
    ads = models.ManyToManyField(Business, through="BusinessAd")
    image = models.ImageField(upload_to='files/ad', null=True)
    bg_color = models.CharField(max_length=255, null=True)
    border_color = models.CharField(max_length=255, null=True)
    button_color = models.CharField(max_length=255, null=True)


class BusinessAd(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
