from django.db import models
from django.urls import reverse
# Create your models here.
CHOICES = [
    'We work together in the same team or on the same project',
    'Blaise was under my responsability',
    'I was under his responsability',
    'We work together inderectly',
    "I was his customer",
    "I heard about his skills",
]

class Recommendation (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    relationship = models.CharField(max_length=200,choices=CHOICES)
    comment = models.TextField(max_length=1000,blank=True,null=True,default=None)

    def get_absolute_url(self):
        return reverse("recommendation_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
        
    
