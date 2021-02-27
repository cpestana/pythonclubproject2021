from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'Club01/index.html')

def Resources(request):
    Resource_list=Resource.objects.all()
    return render(request, 'Club01/Resource.html', {'Resource_list': Resource_list})

def Meetings(request):
    Meeting_list=Meeting.objects.all()
    return render(request, 'Club01/Meeting.html', {'Meeting_list': Meeting_list})

def meetingdetail (request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render (request, 'Club01/meetingdetail.html', {'meet' : meet})

@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)

        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else: 
        form=MeetingForm()

    return render(request, 'Club01/newmeeting.html', {'form': form})

def newResource(request):
     form=ResourceForm

     if request.method=='POST':
          form=ResourceForm(request.POST)

          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()

     return render(request, 'Club01/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'Club01/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Club01/logoutmessage.html')