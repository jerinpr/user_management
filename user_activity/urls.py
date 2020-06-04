from django.urls import path

from user_activity import views

urlpatterns = [
    path('list-user-activity/', views.ListUserActivity.as_view(), name='list-user-activity')

]