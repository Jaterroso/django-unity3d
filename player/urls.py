from django.urls import path
from . import views

urlpatterns = [
    path('player/', views.index, name='index'),
]