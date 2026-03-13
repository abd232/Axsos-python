from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login_register),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
]
