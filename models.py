from django.db import models

# Create your models here.

class FeedBack =(models.Model):
     coustomer = models.CharField(max_length=255)
     rating =models.ImageField()
     comments = models.TextField(blank=True,null=True)

     