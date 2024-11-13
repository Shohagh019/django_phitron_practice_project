from django.urls import path
from . import views
urlpatterns = [
    path('musicians/', views.musician , name= 'musician'),
]