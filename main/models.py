from django.db import models
from django.conf import settings
# Create your models here.
class TeacherInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    subject = models.CharField(max_length=50)
    classes = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    def __str__(self):
        return str(self.name)+" "+str(self.email)+" "+str(self.subject)+" "+str(self.classes)+" "+str(self.phone_number)


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    std = models.CharField(max_length=50)
    class_section = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    rollno = models.IntegerField()
    def __str__(self):
        return str(self.name)+" "+str(self.email)+" "+str(self.std)+" "+str(self.class_section)+" "+str(self.stream)+" "+str(self.rollno)