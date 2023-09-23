from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, User
from .serialized import MessageSerializer, UserRegistrationSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class UsersHandler(generics.ListAPIView):
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


class UserMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Message.objects.filter(user_id=user_id)
        return queryset
