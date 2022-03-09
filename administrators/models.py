from django.db import models

# Create your models here.
class Log(models.Model):
    logDetails = models.TextField(null=True)
    class Meta:
        db_table = 'logs'
