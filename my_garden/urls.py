from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_plant/', views.add_plant, name="add_plant"),
    path('manage_plant/<pk>/', views.manage_plant, name="manage_plant"),
]
