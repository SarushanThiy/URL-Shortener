from django.urls import path
from . import views

urlpatterns = [
    path('', views.shortener, name='shortener' ),
    path('<str:shortened_link>/', views.link_redirect, name="redirect")
]
