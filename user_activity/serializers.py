from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

from user_activity.models import UserProfile, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField('_start_time')
    end_time = serializers.SerializerMethodField('_end_time')
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

    def _start_time(self, value):
        if value.start_time:
            new_start_date= datetime.strftime(value.start_time, " %B %d %Y %I:%M %p")
            return new_start_date
    def _end_time(self, value):
        if value.end_time:
            new_end_date= datetime.strftime(value.end_time, " %B %d %Y %I:%M %p")
            return new_end_date 

class UserProfileSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(required= False)
    class Meta:
        model = UserProfile
        fields = ['custom_id','real_name','tz','activity_periods']
    def create(self, validated_data):
        validated_data['user'] = User.objects.create(username=validated_data.get('custom_id'), email=validated_data.get('email'))
        user_obj = UserProfile.objects.create(**validated_data)
        return user_obj

