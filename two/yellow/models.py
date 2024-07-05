from django.db import models

# Create your models here.
class yellow_M(models.Model):
    
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Course = models.CharField( max_length=200)
    Phone = models.CharField(max_length=200)
    College = models.CharField(max_length=200)



    def __str__(self):
        return self.Course