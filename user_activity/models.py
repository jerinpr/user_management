from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    custom_id = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    activity_periods = models.ForeignKey('user_activity.ActivityPeriod',null=True,on_delete=models.CASCADE)
    

class ActivityPeriod(models.Model):
    start_time =  models.DateTimeField(default= timezone.now(),blank=True, null=True)
    end_time =  models.DateTimeField(default= timezone.now(),blank=True, null=True)


