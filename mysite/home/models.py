from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=True,max_length=122)
    email = models.CharField(blank=True,max_length=122)
    phone = models.CharField(blank=True,max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    