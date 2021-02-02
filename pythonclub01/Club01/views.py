from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your views here.
def index(request):
    return render(request, 'Club01/index.html')

def Resources(request):
    Resource_list=Resource.objects.all()
    return render(request, 'Club01/Resource.html', {'Resource_list': Resource_list})

def Meetings(request):
    Meeting_list=Meeting.objects.all()
    return render(request, 'Club01/Meeting.html', {'Meeting_list': Meeting_list})

def Eventss(request):
    Event_list=Event.objects.all()
    return render(request, 'Club01/Events.html', {'Event_list': Event_list})

def MeetingMinutess(request):
    MeetingMinutes_list=MeetingMinutes.objects.all()
    return render(request, 'Club01/MeetingMinutes.html', {'MeetingMinutes_list': MeetingMinutes_list})