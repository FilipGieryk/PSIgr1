from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import FriendRequest, User
from .serializers import UserSerializer, FriendSerializer
from base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/friends',
        'GET /api/users/:id'
        'GET /api/friends/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getFriends(request):
    friends = FriendRequest.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFriend(request, pk):
    friend = FriendRequest.objects.get(id=pk)
    serializer = UserSerializer(friend, many=False)
    return Response(serializer.data)