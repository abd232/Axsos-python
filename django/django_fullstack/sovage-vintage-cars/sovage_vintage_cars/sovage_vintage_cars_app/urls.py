from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.log_in),
    path('cars', views.cars),
    path('logout', views.log_out),
    path('cars/new', views.newcar),\
    path('cars/<int:id>', views.car),
    path('cars/<int:id>/buy', views.buy_car),
    path('cars/<int:id>/unbuy', views.unbuy_car),
    path('cars/edit/<int:id>', views.edit_car),
    path('cars/remove/<int:id>', views.remove_car),
    path('users/<int:id>', views.user_purcheses),
]
