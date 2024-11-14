from django.shortcuts import render, redirect
from .forms import MusicianForm
from . import models
def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
    else:
        form = MusicianForm()        
    return render(request, 'musician.html', {'form': form})


def edit_musician(request, id):
    music = models.Musician.objects.get(pk=id)
    music_form = MusicianForm(instance= music)
    if request.method == 'POST':
        music_form = MusicianForm(request.POST, instance = music)
        if music_form.is_valid():
            music_form.save()
            return redirect('home')      
    return render(request, 'musician.html', {'form': music_form})