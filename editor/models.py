from django.db import models
from datetime import datetime
# Create your models here.


class Coder(models.Model):
    code_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    code_title = models.CharField(max_length=30)
    preference = models.CharField(max_length=7)
    date = models.DateTimeField(default=datetime.now()z, blank=True)

    def __str__(self):
        return self.code_title
