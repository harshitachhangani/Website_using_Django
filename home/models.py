from django.db import models

# Commands to be used after registering apps and models:
# python manage.py makemigrations & python manage.py migrate
# make migrations: create and store in a file
# migrate: apply the pending changes created by the makemigrations

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobno = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

    