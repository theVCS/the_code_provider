from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30, verbose_name='Name')
    email_id = models.EmailField(blank=True, verbose_name='Email ID')
    friends = models.ManyToManyField(User, related_name='friends_list')
    followers = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user, name, email_id):
        profile = cls(user=user, name=name, email_id=email_id)
        return profile


class FriendRequest(models.Model):
    request_by = models.ForeignKey(User, related_name='request_by', on_delete=models.CASCADE)
    request_to = models.ForeignKey(User, related_name='request_to', on_delete=models.CASCADE)
    send_time = models.DateTimeField(default=datetime.now)
    status = models.CharField(default="pending", max_length=10)

    @classmethod
    def create(cls, request_by, request_to):
        friend_request = cls(request_by=request_by, request_to=request_to)
        return friend_request
