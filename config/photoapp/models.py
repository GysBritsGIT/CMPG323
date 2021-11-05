'''Photoapp Models'''

from django.db import models

from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

class Photo(models.Model):
    
    geolocation = models.CharField(max_length=100)
    
    description = models.CharField(max_length=250) 

    created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='photos/')

    personSubmit = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    tags = TaggableManager() 

    def __str__(self):
        return self.title