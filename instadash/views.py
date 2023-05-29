from instadash.models import User, Ad
from django.http import JsonResponse
from instadash.serializers import UserSerializer, AdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
    data = Ad.objects.all()
    serializer = AdSerializer(data, many=True)
    return JsonResponse({'ads': serializer.data})
