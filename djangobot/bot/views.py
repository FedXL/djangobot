from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, User
from .serialized import MessageSerializer, UserRegistrationSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class UsersHandler(generics.ListAPIView,
                   generics.UpdateAPIView,
                   generics.DestroyAPIView):
    serializer_class = UserRegistrationSerializer

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
        """change name or password """
        try:
            user = User.objects.get(login=request.data.get('login'))
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
        """delete user"""
        try:
            user = User.objects.get(login=request.data.get('login'))
            user.delete()
            return Response({'answer': 'success user was deleted'})
        except User.DoesNotExist:
            return Response({'answer': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ER:
            return Response({'answer': 'error cannot delete user'})

class CreateToken(generics.ListAPIView):



class UserMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Message.objects.filter(user_id=user_id)
        return queryset
