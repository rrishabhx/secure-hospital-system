from django.conf import settings
from django.db import models


# Create your models here.
class HospitalStaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=70,null=True)
    role  = models.CharField(max_length=20,null=True)
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'
        
    class Meta:
        db_table = 'staff'
