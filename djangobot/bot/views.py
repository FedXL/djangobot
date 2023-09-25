import random
import string

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .custom_auth import CustomJWTAuthentication
from .models import User, TeleUser, Token, Message
from .serialized import MessageSerializer, UserRegistrationSerializer, UserCheckSerializer, MessagesSerializer
from .utils import is_authenticate, create_token, get_user_by_bot_token, send_message_to_bot, create_bot_token, \
    save_message, check_code


class HelloWorld(APIView):
    authentication_classes = [CustomJWTAuthentication]  # Используем ваш кастомный аутентификационный класс

    def get(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({"message": "Доступ запрещен"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message": f"Привет, {user.name}!"})


class UsersHandler(generics.ListAPIView,
                   generics.UpdateAPIView,
                   generics.DestroyAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = [CustomJWTAuthentication]

    def post(self, request):
        """Create user"""
        serializer = self.serializer_class(data=request.data)
        if User.objects.filter(login=request.data.get('login')).exists():
            return Response({'answer': 'login is already used'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'answer': 'success'}, status=status.HTTP_400_BAD_REQUEST)
            except IntegrityError:
                return Response({'answer': 'login is already used'})
        else:
            return Response({"answer": "data is invalid"})

    def update(self, request):
        """change name or psw"""
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({"message": "Доступ запрещен"}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(login=user.login)
        except User.DoesNotExist:
            return Response({'answer': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"answer": "success data was changed"})
            except Exception as ER:
                return Response({"answer": "update error"})
        else:
            return Response({"answer": "data is invalid"})

    def destroy(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({"message": "Доступ запрещен"}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(login=user.login)
            user.delete()
            return Response({'answer': 'success user was deleted'})
        except User.DoesNotExist:
            return Response({'answer': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ER:
            return Response({'answer': 'error cannot delete user'})


class JwtObrainView(generics.ListAPIView):
    serializer_class = UserCheckSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'answer': 'invalid input data'})
        login = request.data.get('login')
        psw = request.data.get('psw')
        if is_authenticate(login, psw):
            token = create_token(login)
            return Response({'answer': 'success', 'access_token': token})





class CabinetUserView(generics.CreateAPIView,
                      generics.RetrieveAPIView):
    authentication_classes = [CustomJWTAuthentication]

    def post(self, request, *args, **kwargs):
        """generate bot token"""
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({'answer': "access denied"})
        code = request.data.get('code')
        if check_code(user, code):
            token = create_bot_token(user)
            return Response({'answer': 'success', 'bot_token': token})
        else:
            return Response({'error': 'i dont understand why'})

    def get(self, request, *args, **kwargs):
        """get message history"""
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({"answer": "access denied"})
        messages = Message.objects.filter(user=user).order_by('-time').all()
        serializer = MessagesSerializer(messages, many=True)
        return Response({"answer": "success",
                         "messages":serializer.data,
                         "name":user.name})


class MessagesView(APIView):
    serializer_class = MessageSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({"answer": "message data is not valid"})
        token = serializer.validated_data.get('bot_token')
        user, user_in_telegram = get_user_by_bot_token(token)
        if not user or not user_in_telegram:
            return Response({'answer': 'invalid token'})
        send_message_to_bot(name=user.name,
                            user_id=user_in_telegram.telegram_user_id,
                            text=serializer.validated_data.get('text'))

        del serializer.validated_data['bot_token']
        serializer.validated_data['user'] = user
        # serializer.validated_data['time'] =
        serializer.save()

        # save_message(message_type='Text',
        #              message_text=serializer.validated_data.get('text'),
        #              user=user)

        return Response({"answer": "message was successfully send"})

    def get(self, request):
        return Response({'answer': "all messages from user"})
