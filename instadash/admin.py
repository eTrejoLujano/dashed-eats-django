from django.contrib import admin
from instadash.models import User, Cart, Store, Item, Ad, StoreAd, SavedStore, FoodType, Category, Dashboard, StoreType, StoreCategory, StoreDashboard, Location, OrderHistory

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Ad)
admin.site.register(StoreAd)
admin.site.register(SavedStore)
admin.site.register(FoodType)
admin.site.register(Category)
admin.site.register(Dashboard)
admin.site.register(StoreType)
admin.site.register(StoreCategory)
admin.site.register(StoreDashboard)
admin.site.register(Location)
admin.site.register(OrderHistory)
