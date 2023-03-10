from django.urls import path

from question import views

app_name = "question"

urlpatterns = [
    path('', views.index, name='index'),      # config/urls 에서 작성한 경로 + 해당 파일에서 작성한 경로 ("question/" + "")
    path("<int:question_id>/", views.detail, name='detail'),
    path("answer/create/<int:question_id>/", views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]