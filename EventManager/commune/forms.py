from django import forms
from .models import Event,Participant

class DateInput (forms.DateInput):
    input_type = 'date'

class TimeInput (forms.TimeInput):
    input_type = 'time'

class PasswordInput (forms.PasswordInput):
    input_type = 'password'
    label = 'your pass'

class EmailInput (forms.EmailInput):
    input_type = 'email'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        
        widgets = {
            'FromDate' : DateInput(attrs={'class': "mr-sm-2"}),
            'ToDate' : DateInput(attrs={'class': "mr-sm-2"}),
            'RegEndDate' : DateInput(attrs={}),
            'FromTime' : TimeInput(attrs={}),
            'ToTime' : TimeInput(attrs={}),
            'RegEndTime' : TimeInput(attrs={}),
            'HostEmail' : EmailInput(attrs={}),
            'HostPassword' : PasswordInput(),
            }
        exclude = ()

class ParticipantForm(forms.ModelForm):
    class Meta:
        model=Participant
        exclude = ()