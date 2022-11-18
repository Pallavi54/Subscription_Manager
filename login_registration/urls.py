from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('log', views.Login, name='log'),
    path('next', views.next, name='next'),

]