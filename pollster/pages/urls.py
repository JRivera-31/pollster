from django.urls import path

# from all import views
from . import views

# basically creating routes
urlpatterns = [
    path('', views.index, name='index'),
]