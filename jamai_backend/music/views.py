from django.shortcuts import render
from .models import Song


def home(request):
    return render(request, 'music/home.html')

def create_song(request):
    return render(request, 'music/create_song.html')

def join_session(request):
    return render(request, 'music/join_session.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})
