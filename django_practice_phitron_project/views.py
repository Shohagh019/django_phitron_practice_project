from django.shortcuts import render
from musicians_app.models import Musician
from albums_app.models import Album
# Create your views here.
def home(request):
    data = Album.objects.all()
    return render(request, 'base.html', {'data': data})