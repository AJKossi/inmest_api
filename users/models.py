from django.db import models

# Create your models here.

# Create your models here.
class IMUser(models.Model):

  class UserType(models.TextChoices):
        EIT = "EIT", ("EIT")
        TEACHING_FELLOW= "TEF",("TEACHING_FELLOW")
        ADMIN_STAFF = "ADS", ("ADMIN_STAFF")
        ADMIN = "ADM", ("ADMIN")

  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=False)
  user_type = models.CharField(max_length=3,choices=UserType.choices,default=UserType.EIT)
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

