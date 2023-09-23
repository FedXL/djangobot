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

