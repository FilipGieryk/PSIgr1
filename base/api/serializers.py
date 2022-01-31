from rest_framework.serializers import ModelSerializer
from base.models import User,FriendRequest

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FriendSerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'