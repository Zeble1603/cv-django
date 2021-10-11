from django.db import models
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    mail = models.EmailField(max_length = 254)
    text = models.TextField()
    read = models.BooleanField(default = False)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.mail

    def is_read(self):
        self.read = True
        self.save()