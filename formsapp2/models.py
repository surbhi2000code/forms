from django.db import models

class MakeForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default="")

    def __str__(self):
        return self.first_name
# Create your models here.
