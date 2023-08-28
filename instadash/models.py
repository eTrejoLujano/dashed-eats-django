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


class Store(models.Model):
    class expensive(models.TextChoices):
        cheap = '$'
        budget = '$$'
        expensive = '$$$'
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='src/assets/store', null=True)
    logo = models.ImageField(upload_to='src/assets/store/logo', null=True)
    users = models.ManyToManyField(User, through="SavedStore")
    open_time = models.TimeField()
    close_time = models.TimeField()
    expensive_rating = models.CharField(choices=expensive.choices)


class Item(models.Model):
    name = models.CharField(max_length=200)
    prices = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=4000, null=True)
    users = models.ManyToManyField(User, through="Cart")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='src/assets/items', null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    isCart = models.BooleanField(default=True)


class Ad(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True)
    stores = models.ManyToManyField(Store, through="StoreAd")
    image = models.ImageField(upload_to='src/assets/ads', null=True)
    bg_color = models.CharField(max_length=255, null=True)
    border_color = models.CharField(max_length=255, null=True)
    button_color = models.CharField(max_length=255, null=True)


class StoreAd(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class SavedStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FoodType(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='src/assets/foodtype', null=True)
    stores = models.ManyToManyField(Store, through="StoreType")


class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='src/assets/category', null=True)
    stores = models.ManyToManyField(Store, through="StoreCategory")


class Dashboard(models.Model):
    name = models.CharField(max_length=500)
    stores = models.ManyToManyField(Store, through="StoreDashboard")
    forHome = models.BooleanField(default=True)


class StoreType(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)


class StoreCategory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class StoreDashboard(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)


class Location(models.Model):
    address = models.CharField(max_length=4000, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13)
    latitude = models.DecimalField(max_digits=16, decimal_places=13)
    date_accessed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CategoryDashboard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
