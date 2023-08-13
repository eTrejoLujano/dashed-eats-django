from instadash.models import User, Ad, Store, StoreAd, Dashboard, Category, FoodType, Item
from django.http import JsonResponse, HttpResponse
from instadash.serializers import UserSerializer, RegisterSerializer, DashSerializer, AdSerializer, StoreSerializer, CategorySerializer, FoodTypeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Prefetch
import requests
import os


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)


def users(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return JsonResponse({'users': serializer.data})


def ads(request):
    data = Ad.objects.all().prefetch_related('storead_set')
    serializer = AdSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def getStoreAds(request):
    print("request information", request.data)
    # data = Ad.objects.filter().prefetch_related('storead_set')
    # serializer = AdSerializer(data, many=True)
    # return JsonResponse(serializer.data, safe=False)


def getDashStores(request):
    stores = Dashboard.objects.prefetch_related('stores')
    serializer = DashSerializer(stores, many=True)
    return JsonResponse(serializer.data, safe=False)


def getCategories(request):
    categories = Category.objects.all().order_by('id')
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)


def getFoodType(request):
    foodtypes = FoodType.objects.all().order_by('id')
    serializer = FoodTypeSerializer(foodtypes, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getSavedStores(request):
    stores = Store.objects.filter(savedstore__user__id=1).prefetch_related(
        Prefetch('users', queryset=User.objects.filter(id=1)))
    serializer = StoreSerializer(stores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getStore(request):
    stores = Store.objects.filter(id=request.query_params.get('store_id')).prefetch_related(
        Prefetch('item_set', queryset=Item.objects.all().order_by('id')))
    serializer = StoreSerializer(stores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getCategoryPick(request):
    stores = Category.objects.filter(id=request.query_params.get(
        'category_id')).prefetch_related('storecategory_set')
    serializer = CategorySerializer(stores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getFoodTypePick(request):
    stores = FoodType.objects.filter(name=request.query_params.get(
        'foodtype_name')).prefetch_related('storetype_set')
    serializer = FoodTypeSerializer(stores, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getRestaurants(request):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restuarants&key='
    key = os.environ['GOOGLE_KEY']
    url = url+key
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return HttpResponse(response.text)


@api_view(['GET'])
def getFastFood(request):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=fast%20food&key='
    key = os.environ['GOOGLE_KEY']
    url = url+key
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return HttpResponse(response.text)
