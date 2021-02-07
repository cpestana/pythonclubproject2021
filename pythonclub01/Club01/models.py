from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField()

    def __str__(self):
        return self.meetingTitle
    
    class Meta: 
        db_table='Meeting'
        verbose_name_plural='Meetings'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, null=False, on_delete=models.CASCADE)
    meetingattendance=models.ManyToManyField(User, blank=True)
    meetingminutesText=models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.meetingminutesText

    class Meta: 
        db_table='MeetingMinutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resoucetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourcedateentered=models.DateField()
    resourcedescription=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.resourcename

    class Meta: 
        db_table='Resource'
        verbose_name_plural='Resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.eventtitle

    class Meta: 
        db_table='event'
        verbose_name_plural='events'
        