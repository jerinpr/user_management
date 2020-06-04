from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from user_activity.models import UserProfile, ActivityPeriod
from json import loads, dumps
from collections import OrderedDict

from user_activity.serializers import UserProfileSerializer, ActivityPeriodSerializer
# Create your views here.

class ListUserActivity(APIView):
    serializer_class = UserProfileSerializer
    def get(self, request):
        user_activity_data = UserProfile.objects.all()
        user_activity_dump = UserProfileSerializer(user_activity_data, many=True).data
        # user_activity_dict = loads(user_activity_dump)
        # user_activity_return_list = {}
        # user_activity_return_list['ok'] = 'true'
        # user_activity_return_list['members'] = user_activity_dict
        return Response({"ok": True, "msg":"User activity listed", 'members': user_activity_dump},
                            status=status.HTTP_200_OK)
    