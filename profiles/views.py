from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders a list of all profiles available.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of profiles.
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders a profile page for a specific user.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile page is being rendered.

    Returns:
        HttpResponse: The rendered HTML page displaying the profile page for the specified user.
    """

    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.exception(f"Error loading profile '{username}': {e}")
        raise
