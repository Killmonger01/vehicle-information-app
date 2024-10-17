from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.index, name='index'),
    path('car_detail/<int:car_id>', views.car_detail, name='car_detail'),
    path('add/', views.add_car, name='add_car'),
    path('edit/<int:car_id>/', views.edit_car, name='edit_car'),
    path('car/delete/<int:car_id>/', views.delete_car, name='delete_car'),
]
