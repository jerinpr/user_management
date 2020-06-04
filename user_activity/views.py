from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_activity.serializers import UserProfileSerializer, ActivityPeriodSerializer
# Create your views here.

class CreateUser(APIView):
    serializer_class = UserProfileSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            new_user= serializer.create(validated_data)
            return Response({"status": True, "msg":"User created", 'response': ""},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": False, "msg": "", 'response': {'errors': serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
