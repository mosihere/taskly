from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'phone_number', 'first_name', 'last_name']
    

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'phone_number', 'password', 'first_name', 'last_name']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError('Phone number must be 11 digits long and contain only numbers.')
        
        return value


from djoser.serializers import UserDeleteSerializer as BaseUserDeleteSerializer

class UserDeleteSerializer(serializers.Serializer):
    """
    Serializer to allow deletion of a user without requiring a current password.
    This can be left empty to prevent deletion for regular users.
    """
    pass