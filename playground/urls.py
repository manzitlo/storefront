from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('goodluck/', views.say_hello)
]