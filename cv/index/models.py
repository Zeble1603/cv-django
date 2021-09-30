from django.db import models

# Create your models here.

class Message(models.Model):
    mail = models.EmailField(max_length=254)
    text = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.mail
    
    