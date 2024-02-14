from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class IMUser(AbstractUser):
        UserTypes = [
          ('EIT', ('EIT')),
          ('TEF', ('TEACHING_FELLOW')),
          ('ADS', ('ADMIN_STAFF')),
          ('ADM', ('ADMIN')),
        ]
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)
        user_type = models.CharField(max_length=3,choices=UserTypes)
        date_created=models.DateTimeField(auto_now_add=True)

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohort_member_author')

    def __str__(self):
     return f"{self.member.first_name}"

