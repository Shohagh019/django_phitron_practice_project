from django import forms
from . models import Album

class AlbumForm(forms.ModelForm):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    album_rating = forms.ChoiceField(choices=RATING_CHOICES, label="Album Rating")
    
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {'release_date': forms.DateInput(attrs={'type': 'date'})}