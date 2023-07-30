from django.db import models

# Create your models here.
# Models = table
# lnik, uuid = fields of table
class Url(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=30)

    def __str__(self):
        return self.uuid