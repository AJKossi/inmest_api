from django.db import models

from users.models import Cohort, IMUser

# Create your models here.
class Course(models.Model):
  course_name = models.CharField(max_length=255)
  course_description = models.TextField(blank=True,null=True)
  date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
  date_modified=models.DateTimeField(auto_now=True,blank=True,null=True)

class ClassSchedule(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    REPEAT_FREQUENCY_CHOICES = [
        ('D', ('Daily')),
        ('W', ('Weekly')),
        ('M', ('Monthly')),
        ('Y', ('Yearly')),
    ]
    repeat_frequency = models.CharField(max_length=1, choices=REPEAT_FREQUENCY_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.CharField(max_length=255)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='class_attendance_author')

class Query(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='assigned_queries')
    RESOLUTION_STATUS_CHOICES = [
        ('P', ('PENDING')),
        ('I', ('IN_PROGRESS')),
        ('D', ('DECLINED')),
        ('R', ('RESOLVED')),
    ]
    resolution_status = models.CharField(max_length=1, choices=RESOLUTION_STATUS_CHOICES, default='P')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='query_author')

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='query_comment_author')