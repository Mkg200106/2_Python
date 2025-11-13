from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess_number, name='guess_number'),
    path('reset/', views.reset_game, name='reset_game'),
]
