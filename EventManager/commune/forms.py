from django import forms
from .models import Event,Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ()

class ParticipantForm(forms.ModelForm):
    class Meta:
        model=Participant
        exclude = ()