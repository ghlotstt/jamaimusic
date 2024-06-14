from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('songs/', views.song_list, name='song_list'),
    path('create/', views.create_song, name='create_song'),
    path('join/', views.join_session, name='join_session'),
]
