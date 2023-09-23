from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Message





class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'login', 'psw')
        extra_kwargs = {'psw': {'write_only': True}}

    def create(self, validated_data):
        # Используйте make_password, чтобы хешировать пароль
        validated_data['psw'] = make_password(validated_data['psw'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # При обновлении пароля также используйте make_password
        if 'psw' in validated_data:
            validated_data['psw'] = make_password(validated_data['psw'])
        return super().update(instance, validated_data)

