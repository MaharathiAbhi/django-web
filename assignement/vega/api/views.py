from rest_framework import viewsets
from app.models import *
from api.serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class exam(viewsets.ModelViewSet):
    try:
        queryset = Messages.objects.all()
        serializer_class = MessageSerializer
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
    except Exception as ee:
        Response("hello", status=status.HTTP_404_NOT_FOUND)


class register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
