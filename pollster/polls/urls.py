from django.urls import path

# from all import views
from . import views

app_name = 'polls'
# basically creating routes
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results')
]