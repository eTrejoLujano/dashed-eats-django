from instadash.models import User, Ad
from django.http import JsonResponse
from instadash.serializers import UserSerializer, AdSerializer


def users(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return JsonResponse({'users': serializer.data})


def ads(request):
    data = Ad.objects.all()
    serializer = AdSerializer(data, many=True)
    return JsonResponse({'ads': serializer.data})
