from django.shortcuts import render, redirect
from .forms import MusicianForm
def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
    else:
        form = MusicianForm()        
    return render(request, 'musician.html', {'form': form})