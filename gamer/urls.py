from django.urls import path

from gamer import views

app_name = "gamer"

urlpatterns = [
    path('', views.index, name="index"),
    path('csv_read/', views.csvRead, name='alldata_read'),
    path('<str:match_id>/', views.detail, name='detail'),
]