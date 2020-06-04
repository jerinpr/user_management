from rest_framework import serializers
from django.contrib.auth.models import User

from user_activity.models import UserProfile, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

class UserProfileSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(required= False)
    class Meta:
        model = UserProfile
        fields = ['custom_id','real_name','tz','activity_periods','email']
    def create(self, validated_data):
        validated_data['user'] = User.objects.create(username=validated_data.get('custom_id'), email=validated_data.get('email'))
        user_obj = UserProfile.objects.create(**validated_data)
        return user_obj

