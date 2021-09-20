from django.db import models
from django.urls import reverse
# Create your models here.
CHOICES = [
    ('we work together in the same team or on the same project','We work together in the same team or on the same project'), 
    ('blaise was under my responsability','Blaise was under my responsability'),
    ('i was under his responsability','I was under his responsability'),
    ('we work together inderectly','We work together inderectly'),
    ("i was his customer","I was his customer"),
    ("i heard about his skills","I heard about his skills"),
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
        
    
