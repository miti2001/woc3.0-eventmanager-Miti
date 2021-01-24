from django.shortcuts import render,HttpResponse,redirect
from django import forms
from .forms import EventForm,ParticipantForm
from .models import Event,Participant
from django.core.mail import send_mail
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
        content = Event.objects.filter(id = eventid, HostPassword = eventpass).values('EventName')
        print(content)

        value = content|
        print(value)
        
        key = value['EventName']
        
        part = Participant.objects.filter(EventReg = str(key)).values_list()
        print(part)
        
        return render(request, 'host.html', {
            part : 'part',
        }) 

def participantReg(request):
    content = Event.objects.filter(RegEndDate__gte = datetime.date.today()).order_by('RegEndDate').values(
        'id','EventName', 'Desc', 'Loc', 'FromDate', 'ToDate', 'RegEndDate',
    )

    form = ParticipantForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponse('Saved')
        
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
            name = request.POST['EventName']
            """
            content = Event.objects.filter(EventName = name).values('pk')
            print(content)
            var = content.pop()
            print(var)
            iden = var.get('pk')
            print(iden)
            #send mail

            send_mail(
                'Event successfully registered', # subject
                'Thank you for registering your event with us.'+
                'You have successfully registered your event'+ name +'at commune.'
                'The event id is'+ str(iden) + 'and event password is:'+ (request.POST['HostPassword'])
                +'The event is scheduled from '+ (request.POST['FromDate'])+ (request.POST['FromTime'])+ 
                'to' + (request.POST['ToDate'])+ (request.POST['ToTime'])+
                'You can review the participation for your event at our Commune portal.', # message
                ['mitipurohit27@gmail.com'], # From email
                ['mail'], # To email
            )
            
            """
            return HttpResponse('Saved')
   
def home(request):
    return render(request,'home.html')



