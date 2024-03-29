from rest_framework.serializers import ModelSerializer, EmailField, ValidationError, CharField
from instadash.models import User, Ad, Store, FoodType, Item, Dashboard, Category, StoreAd, StoreDashboard, SavedStore, StoreCategory, Cart, Location, OrderHistory
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
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


class ChangePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class SavedStoreSerializer(ModelSerializer):
    users_info = UserSerializer(source='user')

    class Meta:
        model = SavedStore
        fields = '__all__'


class SavedStoreSerializer(ModelSerializer):
    users_info = UserSerializer(source='user')

    class Meta:
        model = SavedStore
        fields = '__all__'


class SecondStoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    stores_info = SecondStoreSerializer(source='store')

    class Meta:
        model = Item
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    saved_store = SavedStoreSerializer(source='savedstore_set', many=True)
    store_items = ItemSerializer(source='item_set', many=True)

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


class StoreCategorySerializer(ModelSerializer):
    stores_info = StoreSerializer(source='store')

    class Meta:
        model = StoreCategory
        fields = ['stores_info']


class CategorySerializer(ModelSerializer):
    store_category = StoreCategorySerializer(
        source='storecategory_set', many=True)

    class Meta:
        model = Category
        fields = '__all__'


class StoreTypeSerializer(ModelSerializer):
    stores_info = StoreSerializer(source='store')

    class Meta:
        model = StoreCategory
        fields = ['stores_info']


class FoodTypeSerializer(ModelSerializer):
    store_foodtype = StoreTypeSerializer(
        source='storetype_set', many=True)

    class Meta:
        model = FoodType
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CartSerializer(ModelSerializer):
    items_info = ItemSerializer(source='item')

    class Meta:
        model = Cart
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    cart = CartSerializer(source='cart_set', many=True)

    class Meta:
        model = OrderHistory
        fields = '__all__'
