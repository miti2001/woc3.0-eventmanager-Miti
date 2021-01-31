from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from .forms import EventForm,ParticipantForm
from .models import Event,Participant
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
import os
from twilio.rest import Client
import datetime

# Create your views here.

def host(request):
    if request.method == 'GET':
        part = None
        return render(request, 'host.html', {
            part:'part',
        })

    else:
        eventid = request.POST['eventid']
        eventpass = request.POST['eventpassword']
        part = None

        d = Event.objects.values_list('id')
        tempid = (int(eventid),)
        temppass = (eventpass,)
        
        if(tempid in d):
            content1 = Event.objects.get(id = eventid)
            pass1 = Event.objects.filter(id = eventid).values_list('HostPassword')
           
            if temppass != pass1[0]:
                    messages.error(request,'Wrong password')
                    return redirect('host')

            else:
                part = Participant.objects.filter(EventReg = content1).values_list(
                    'id','Name', 'Contact', 'Email', 'RegType','Number',
                )

                if(not part):
                    messages.error(request,'No participant has registered for the event')
                    return redirect('host')
        else:
            messages.error(request,'This event id is not registered')

        context = {
            "content" : part
        }   
    
        return render(request, 'host.html', context) 
        

def participantReg(request):
    content = Event.objects.filter(RegEndDate__gte = datetime.date.today()).order_by('RegEndDate').values(
        'id', 'EventName', 'Desc', 'Loc', 'FromDate', 'ToDate', 'RegEndDate',
    )

    form = ParticipantForm(request.POST)

    if form.is_valid():

        contact = request.POST['Contact']
        name = request.POST['Name']
        mail = request.POST['Email']
        event = request.POST['EventReg']
        data = Participant.objects.values_list('Email')
        event1 = Participant.objects.filter(Email = mail).values_list('EventReg')

        temp_mail = (mail,)
        temp_event = (event,)

        if(temp_mail in data and temp_event in event1):
            messages.error(request,'You have already registered in this event under the given email id')
        
        else:
            form.save()
            
            account_sid ='ACa828eeca8f45c4c1925d19b55e04c1a1'
            auth_token ='9619835ca235f95a605e6243b7ae6919'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body='Hello '+ name +',\nYour participation for '+event+' is confirmed.',
                                from_='+12817092069',
                                to='+91'+ str(contact),
                            )
           
            return redirect("")
        
    return render(request, 'participantReg.html', {
        'form':form,
        'content':content,
    })

    
    
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
            
            mail = request.POST['HostEmail']
            name = request.POST['EventName']

            send_mail(
                'Successful Event Registration',
                'Hey there! your event has been successfully registered.',
                '',
                [mail],
                fail_silently=False,
            )
            return HttpResponse('Saved')
        
   
def home(request):
    return render(request,'home.html')



