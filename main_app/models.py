from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    decade = models.IntegerField()

    def __str__(self):
        return self.title
        