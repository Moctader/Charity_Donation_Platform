from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name
