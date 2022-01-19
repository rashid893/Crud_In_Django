from django.db import models

# Create your models here.
class Entry(models.Model):
    id1 = models.CharField(max_length=10,primary_key=True)
    id2 = models.CharField(max_length=50)
    id3 = models.CharField(max_length=50)
    def __str__(self):
        return self.id1