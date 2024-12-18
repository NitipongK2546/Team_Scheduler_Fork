from django import forms
from .models import Event

class EventCreationFormSingle(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'start_time', 'end_time', 'text']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date',}),
            'start_time': forms.TimeInput(attrs={'type': 'time',}),
            'end_time': forms.TimeInput(attrs={'type': 'time',}),
        }
    