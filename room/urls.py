from django.urls import path
from .views import room, rooms

urlpatterns = [
    path('<int:pk>/', room),
    path('', rooms)
]