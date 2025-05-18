from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    feedback = models.TextField()