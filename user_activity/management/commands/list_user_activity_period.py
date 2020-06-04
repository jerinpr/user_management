from django.core.management.base import BaseCommand
from user_activity.models import UserProfile, ActivityPeriod
from json import loads, dumps
from collections import OrderedDict

from user_activity.serializers import UserProfileSerializer, ActivityPeriodSerializer


class Command(BaseCommand):
    help = 'list user activity period'
    """
    This command will list the user and their activity periods
    """
    def handle(self, *args, **kwargs):
        user_serializer= UserProfileSerializer
        user_activity_data = UserProfile.objects.all()
        user_activity_dump = dumps(user_serializer(user_activity_data, many=True).data)
        user_activity_dict = loads(user_activity_dump)
        user_activity_return_list = {}
        user_activity_return_list['ok'] = 'true'
        user_activity_return_list['members'] = user_activity_dict
        