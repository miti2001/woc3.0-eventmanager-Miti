from django.shortcuts import render,HttpResponse
from django import forms
from .forms import EventForm
from .models import Event


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