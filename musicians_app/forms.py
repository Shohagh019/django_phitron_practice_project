from django import forms
from . models import Musician
instruments = [
    ('Guitar', 'Guitar'),
    ('Piano', 'Piano'),
    ('Drums', 'Drums'),
    ('Violin', 'Violin'),
    ('Flute', 'Flute'),
    ('Saxophone', 'Saxophone'),
    ('Cello', 'Cello'),
    ('Trumpet', 'Trumpet')
]
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets ={
            'instrument_type': forms.Select(choices=instruments)
        }