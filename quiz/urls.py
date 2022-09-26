from django.urls import path
from quiz.views import Question,Answers


app_name = 'quiz'


urlpatterns = [
    path('', Question.as_view({'get':'list'}), name='Question'),
    path('<str:subject>/', Question.as_view({'get':'retrieve'}), name='Subject'),
    path('<str:subject>/<str:question>/', Answers.as_view(), name='Answers'),

]

