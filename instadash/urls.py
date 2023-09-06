from django.contrib import admin
from django.urls import path
from instadash import views
from .views import MyTokenObtainPairView, RegisterView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', RegisterView.as_view(), name='register'),

    path('api/users/', views.users, name="users"),
    path('api/ads/', views.ads, name="ads"),
    path('api/routes/', views.getRoutes, name='routes'),
    path('api/storeads/', views.getStoreAds, name='storeads'),
    path('api/dashboard/', views.getDashStores, name='dashboard'),
    path('api/categories/', views.getCategories, name='categories'),
    path('api/foodtype/', views.getFoodType, name='foodtype'),
    path('api/storeid/', views.getStoreById, name='storeid'),
    path('api/storename/', views.getStoreByName, name='storename'),
    path('api/allstores/', views.getAllStores, name='allstores'),
    path('api/storecategory/', views.getCategoryPick, name='category'),
    path('api/storetype/', views.getFoodTypePick, name='storetype'),
    path('api/storepickup/', views.getStorePickup, name='storepickup'),
    path('api/fastfood/', views.getFastFood, name='fastfood'),
    path('api/restaurants/', views.getRestaurants, name='restaurants'),
    path('api/coffee/', views.getCoffee, name='coffee'),
    path('api/pizza/', views.getPizza, name='pizza'),
    path('api/grocery/', views.getGrocery, name='grocery'),
    path('api/drugstore/', views.getDrugstore, name='drugstore'),
    path('api/convenience/', views.getConvenience, name='convenience'),
    path('api/distance/', views.getDistance, name='distance'),
    path('api/placedetails/', views.getPlaceDetails, name='placedetails'),
    path('api/address/', views.getAddress, name='address'),
    path('api/latestaddress/', views.getLatestAddress, name='latestaddress'),
    path('api/alladdresses/', views.getAllAddresses, name='alladdresses'),
    path('api/changeaddress/', views.changeAddress, name='changeaddress'),
    path('api/deleteaddress/', views.deleteAddress, name='deleteaddress'),
    path('api/getcart/', views.getCart, name='getcart'),
    path('api/addcart/', views.addCart, name='addcart'),
    path('api/deletecart/', views.deleteCart, name='deletecart'),
    path('api/addonecart/', views.addOneCart, name='addonecart'),
    path('api/minusonecart/', views.minusOneCart, name='minusonecart'),
]
