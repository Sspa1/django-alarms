from django.urls import path, include
from .views import AlarmaList

urlpatterns = [
    path('alarma/', AlarmaList.as_view()),
]