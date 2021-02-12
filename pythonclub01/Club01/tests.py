from django.test import TestCase
from django.config.models import user 
from .models import Meeting, MeetingMinutes, Resource, Event
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


