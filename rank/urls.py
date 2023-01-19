# apps/urls.py

from django.urls import path
from rank import views

app_name = "rank"

urlpatterns = [
    path('', views.index, name="index"),
    path('read_data', views.readData, name="read_data"),
    path('pre_rank/', views.likes, name="pre_rank"),
    # path('pre_rank/', views.predict_rank, name="pre_rank"),
    # path('pre_rank/(?P<id>[\w-]+)/$', views.predict_rank, name="pre_rank"),
]