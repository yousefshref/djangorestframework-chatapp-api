from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view

from .models import Chat, UserProfile
from .serializers import ChatSerializer, UserProfileSerializer
from django.db.models import Q


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    permission_classes = (AllowAny,)


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getFrindsChats(request, sender, reciver):
    chats = Chat.objects.filter(
        Q(whosend=sender+reciver) | Q(whosend=reciver+sender))
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFrindsChatsList(request, sender):
    chats = Chat.objects.all().filter(Q(sender=sender)).values(
        'reciver', 'sender', 'whosend', 'message', 'created',).distinct()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(['POST', "GET"])
def createMessageToFriend(request, sender, reciver):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deleteMessage(request, pk):
    chat = Chat.objects.filter(id=pk)
    chat.delete()
    return Response('deleted')


@api_view(['POST', 'GET'])
def createUserProfile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST', "GET"])
def userProfileUpdate(request, username):
    prof = UserProfile.objects.get(user=username)
    ser = UserProfileSerializer(instance=prof, data=request.data)
    if ser.is_valid(raise_exception=True):
        ser.save()
    return Response(ser.data)


@api_view(['GET', 'POST'])
def getprofile(request, user):
    user = UserProfile.objects.filter(user=user)
    serializer = UserProfileSerializer(user, many=True)
    return Response(serializer.data)
