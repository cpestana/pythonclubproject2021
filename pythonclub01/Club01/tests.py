from django.test import TestCase
from django.config.models import user 
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
import .forms MeetingForm, ResourceForm
import django.urls import reverse_lazy, reverse 
# Create your tests here.

class MeetingTest(TestCase): 
    def setUp(self):
        self.type=Meeting(meetingTitle='First Meeting')
        self.user=User(username='Christine')
    def test_string(self):
        self.assertEqual(str(self.type), 'First Meeting')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class ResourceTest(TestCase):
    def test_string(self):
        self.assertEqual(str(self.type), 'resourcename')

    def test_table(self): 
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        self.assertEqual(str(self.type), 'meetingminutesText')
   
    def test_table(self): 
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'MeetingMinutes')

class EventTest(TestCase):
    def test_string(self): 
        self.assertEqual(str(self.type), 'eventtitle')
    
    def test_table(self): 
        self.assertEqual(str(Event._meta.db_table), 'Event')

class NewMeetingForm(TestCase):
 #valid form data
 def test_meetingform(self):
    data = {
        'meetingTitle':'First Python Project', 
        'meetingDate':'2021-02-21', 
        'meetingTime':'05:30:00', 
        'meetingLocation':'Zoom conference',
        'meetingAgenda':'First Python project discussion', 
     }
    form=MeetingForm (data)
     self.assertTrue(form.is_valid)

class NewResourceForm(TestCase):
 #valid form data
 def test_resourceform(self):
    data = {
        'resourcename':'Full stack Python', 
        'resourcetype':'website', 
        'resourceurl':'https://www.fullstackpython.com/best-python-resources.html', 
        'resourcedateentered':'2021-02-19',
        'resourcedescription':'Good resource for learning Python', 
        'user':'self.u',
     }
    form=ResourceForm (data)
     self.assertTrue(form.is_valid)

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource=Resource.objects.create(resourcename='Full stack Python', resourcetype='website', resourceurl='https://www.fullstackpython.com/best-python-resources.html', resourcedateentered='2021-02-19', resourcedescription='Good resource for learning Python', user=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login?next=/Club01/newresource/')


