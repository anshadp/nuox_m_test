from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('add_teacher2', views.add_teacher2, name='add_teacher2'),
    path('profile', views.profile, name='profile'),
]
