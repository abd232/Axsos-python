from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('increment_by_two', views.increment_by_two),
    path('increment', views.increment),
    path('reset', views.reset),
    path('destroy_session', views.destroy),
]