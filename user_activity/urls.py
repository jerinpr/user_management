from django.urls import path

from user_activity import views

urlpatterns = [
    path('', views.ListUserActivity.as_view(), name='list-user-activity')

]