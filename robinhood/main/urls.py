from main import views
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('us/en/',views.index),
    path('login',views.login)
]