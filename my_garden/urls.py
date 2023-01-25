from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_plant/', views.add_plant, name="add_plant"),
    path('manage_plant/<pk>/', views.manage_plant, name="manage_plant"),
    path('plant_list/', views.plant_list, name="plant_list"),
    path('plant_list/add', views.add_plant_list, name="add_plant_list"),
    path('plant_list/edit/<pk>', views.edit_plant, name="edit_plant")
]
