from django.db import models
from django.urls import reverse

READS = (
    ('B', 'Morning'),
    ('L', 'Noon'),
    ('D', 'Night')
)

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    info = models.CharField(max_length=1000, default='')
    decade = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})

class Reading(models.Model):
    date = models.DateField()
    read = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=READS,
        # set the default value for meal to be 'B'
        default=READS[0][0]
    )

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_read_display()} on {self.date}"

    class Meta:
        ordering = ['-date']