from datetime import timedelta
import json
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
import random
import string

from user_activity.models import UserProfile, ActivityPeriod

class Command(BaseCommand):
    help = 'create user'
    """
    This command create some users whose data are store in a js file which is located at 'user_activity/json_data/create_user_data.json'
    """
    def handle(self, *args, **kwargs):
        try:
            files= open('user_activity/json_data/create_user_data.json')
        except:
            files= None
        if files:
            user_data= json.load(files)
            for each in user_data:
                stringLength = 5
                letters = string.ascii_letters
                random_id= ''.join(random.choice(letters) for i in range(stringLength))
                each['custom_id'] = random_id
                each['user'] = User.objects.create(username=random_id, email= each.get('email'))
                if each.get('activity_periods'):
                    activity_obj= ActivityPeriod.objects.create(start_time=each['activity_periods'].get('start_time'),end_time=each['activity_periods'].get('end_time'))
                    each['activity_periods'] = activity_obj
                user_obj = UserProfile.objects.create(**each)

