from django.shortcuts import render
from musicians_app.models import Musician
# Create your views here.
def home(request):
    data = Musician.objects.all()
    return render(request, 'base.html', {'data': data})