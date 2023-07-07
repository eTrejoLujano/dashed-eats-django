from rest_framework.serializers import ModelSerializer
from instadash.models import User, Ad
# from base.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
