from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30, verbose_name='Name')
    email_id = models.EmailField(blank=True, verbose_name='Email ID')
    friends = models.ManyToManyField(User, related_name='friends_list')

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user, name,email_id):
        profile = cls(user=user, name=name, email_id=email_id)
        return profile
