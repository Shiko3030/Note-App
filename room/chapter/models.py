from django.db import models

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=50)
    note = models.TextField(max_length=1000 , null=True)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title



