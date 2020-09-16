from django.db import models

# Create your models here.


class Coder(models.Model):
    code_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    code_title = models.CharField(max_length=30)
    filter = models.CharField(max_length=7)
    upload_date = models.DateField()

    def __str__(self):
        return self.code_title
