from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError



User = get_user_model()

class UserSerializer(BaseUserSerializer):

    phone_number = serializers.CharField(required=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ['phone_number', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError('Phone number must be 11 digits long and contain only numbers.')
        
        if User.objects.filter(phone_number=value).exists():
            raise ValidationError('A user with this phone number already exists.')
        
        return value

    def create(self, validated_data):
        user_password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(user_password)
        user.save()
        return user