from django.urls import path

# from all import views
from . import views

app_name = 'polls'
# basically creating a route
urlpatterns = [path('', views.index, name='index')]