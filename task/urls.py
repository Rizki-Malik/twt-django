from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:id>", views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
]