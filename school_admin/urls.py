from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('view_teachers', views.view_teachers, name='view_teachers'),
    path('permission/<int:id>', views.permission, name='permission')

]
