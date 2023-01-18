# apps/urls.py

from django.urls import path
from rank import views

app_name = "rank"

urlpatterns = [
    path('', views.index, name="index"),
    path('read_data', views.readData, name="read_data"),
]