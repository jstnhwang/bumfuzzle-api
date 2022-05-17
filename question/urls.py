from django.urls import path
from .views import questions, question

urlpatterns = [
    path('', questions),
    path('<int:pk>/', question),
]