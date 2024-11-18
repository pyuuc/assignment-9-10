from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """Topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """return a str representation of the model"""
        return self.text 

"""Def the entry model"""

class Entry(models.Model):
    """something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        "return a simple string representing the entry"
        return f"{self.text[:50]}..."
    
    
    