from django.urls import path
from . import views
urlpatterns = [
    path('rock',views.rock , name='rock'),
    path('',views.dotsbox , name='dotsbox')
]
