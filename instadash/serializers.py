from rest_framework.serializers import ModelSerializer, EmailField, ValidationError, CharField
from instadash.models import User, Ad, Store, FoodType, Item, Dashboard, Category, StoreAd, StoreDashboard, SavedStore
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class SavedStoreSerializer(ModelSerializer):
    users_info = UserSerializer(source='user')

    class Meta:
        model = SavedStore
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    saved_store = SavedStoreSerializer(source='savedstore_set', many=True)

    class Meta:
        model = Store
        fields = '__all__'


class StoreAdSerializer(ModelSerializer):
    stores_info = StoreSerializer(source='store')

    class Meta:
        model = StoreAd
        fields = ['stores_info']


class AdSerializer(ModelSerializer):
    store_ad = StoreAdSerializer(source='storead_set', many=True)

    class Meta:
        model = Ad
        fields = '__all__'


class StoreDashSerializer(ModelSerializer):
    stores_info = StoreSerializer(source='store')

    class Meta:
        model = StoreDashboard
        fields = ['stores_info']


class DashSerializer(ModelSerializer):
    store_dashboard = StoreDashSerializer(
        source='storedashboard_set', many=True)

    class Meta:
        model = Dashboard
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodTypeSerializer(ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'
