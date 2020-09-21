from django.core.exceptions import PermissionDenied
from .models import Profile,FriendRequest


def user_can_accept_friend_request(function):
    def wrap(request, *args, **kwargs):
        friend_request = FriendRequest.objects.get(pk=kwargs['friend_request_id'])
        if request.user.id != friend_request.request_to:
            raise PermissionDenied
        else:
            return function(request, *args, **kwargs)

    return wrap
