from django.db import models
from django.urls import reverse
from datetime import date

READS = (
    ('B', 'Morning'),
    ('L', 'Noon'),
    ('D', 'Night')
)

class Collectable(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collectables_detail', kwargs={'pk': self.id})

class Comic(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    info = models.CharField(max_length=1000, default='')
    decade = models.IntegerField()
    collectables = models.ManyToManyField(Collectable)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})

class Reading(models.Model):
    date = models.DateField('reading date')
    read = models.CharField(
        max_length=1,
        choices=READS,
        default=READS[0][0]
    )

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_read_display()} on {self.date}"

    class Meta:
        ordering = ['-date']