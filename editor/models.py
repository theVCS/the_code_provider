from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.


class Code(models.Model):
    unique_code_id = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    website = models.CharField(max_length=30)
    problem_title = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10)
    sharing_option = models.CharField(max_length=7)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.unique_code_id

    @classmethod
    def create(cls, user=user, unique_code_id=unique_code_id, website=website, language=language,
               sharing_option=sharing_option, problem_title=""):
        code = cls(unique_code_id=unique_code_id, user=user, website=website, language=language,
                   sharing_option=sharing_option, problem_title=problem_title)
        code.save()
        return code
