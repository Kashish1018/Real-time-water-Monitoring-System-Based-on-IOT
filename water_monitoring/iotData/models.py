from django.utils import timezone
from django.db import models

class IotData(models.Model):
    temperature = models.FloatField()
    pHValue = models.FloatField()
    turbidity = models.FloatField()
    username = models.CharField(max_length=100)  # New field: username
    password = models.CharField(max_length=100)  # New field: password
    salinity = models.FloatField(default = 0.0)  # New field: salinity
    
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject