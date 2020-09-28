from django.db import models

# Create your models here.
class Argorithm(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    url = models.CharField(max_length=200, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title