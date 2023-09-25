from abc import ABC

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Message


class MessageSerializer(serializers.ModelSerializer):
    bot_token = serializers.CharField(max_length=25, min_length=25, allow_blank=False)

    class Meta:
        model = Message
        fields = ('type', 'text', 'bot_token')


class UserCheckSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    psw = serializers.CharField(max_length=50)






class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'login', 'psw')
        extra_kwargs = {'psw': {'write_only': True}}

    def create(self, validated_data):
        validated_data['psw'] = make_password(validated_data['psw'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'psw' in validated_data:
            validated_data['psw'] = make_password(validated_data['psw'])
        return super().update(instance, validated_data)

