from django.contrib import admin
from instadash.models import User, Cart, Business, Item, Ad, BusinessAd

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Business)
admin.site.register(Item)
admin.site.register(Ad)
admin.site.register(BusinessAd)
