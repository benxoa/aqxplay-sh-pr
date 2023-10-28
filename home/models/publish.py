from django.db import models


class Publish(models.Model):
    title = models.CharField(max_length=20)
    
    
    image = models.ImageField(upload_to='upload/')
    def __str__(self):
        return self.title