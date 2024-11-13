from django import forms
from . models import Musician
instruments = [
    ('g', 'Guitar'),
    ('p', 'Piano'),
    ('d', 'Drums'),
    ('v', 'Violin'),
    ('f', 'Flute'),
    ('s', 'Saxophone'),
    ('c', 'Cello'),
    ('t', 'Trumpet')
]
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets ={
            'instrument_type': forms.Select(choices=instruments)
        }