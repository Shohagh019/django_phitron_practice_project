from django.urls import path
from . import views
urlpatterns = [
    path('musicians/', views.musician , name= 'musician'),
    path('edit_musicians/<int:id>', views.edit_musician , name= 'edit_musician'),
]