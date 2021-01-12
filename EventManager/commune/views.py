from django.shortcuts import render,HttpResponse
from django import forms
from .forms import EventForm,ParticipantForm
from .models import Event,Participant


# Create your views here.
def home(request):
    return render(request,'home.html')

def eventReg(request):
    if request.method == 'GET':
        form = EventForm
        return render(request, 'eventReg.html', {
            'form':form,
    })

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')

def participantReg(request):
    content = Event.objects.all().values_list(
        'EventName', 'Desc', 'Loc', 'FromDate', 'ToDate', 'RegEndDate',
    )
    
    if request.method == 'GET':
        form = ParticipantForm
        return render(request, 'participantReg.html', {
            'content':content,
            'form':form,
    })

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')