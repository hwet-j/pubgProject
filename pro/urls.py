# apps/urls.py

from django.urls import path
from pro import views

app_name = "pro"

urlpatterns = [
    path('', views.index, name="index"),
    path('match/<str:match_id>/', views.detail, name='detail'),
    path('readCsv/', views.csvRead, name='match_data_read'),


]