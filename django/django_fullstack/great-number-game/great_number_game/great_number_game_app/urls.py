from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('guess', views.guess, name='guess'),
    path('save_leaderboard', views.save_leaderboard, name='save_leaderboard'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('reset', views.reset, name='reset'),    
]