from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('admin-dashboard', views.dashboard),
    path('users/show/<int:id>', views.profile),
    path('massage/<int:for_user_id>', views.massage)
]
