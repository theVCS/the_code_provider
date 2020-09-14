from django import template
from django.apps import apps
from django.contrib.auth.models import User

register = template.Library()
FriendRequest = apps.get_model('profiles', 'FriendRequest')


@register.simple_tag()
def is_pending_request_exists(request_by, request_to):
    friend_request = FriendRequest.objects.filter(request_by=request_by, request_to=request_to).count()
    if friend_request > 0:
        return "True"
    return "False"
