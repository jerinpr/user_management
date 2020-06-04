from django.urls import path

from user_activity import views

urlpatterns = [
    path('create-user/', views.CreateUser.as_view(), name='create-user')

]