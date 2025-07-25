from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders a list of all lettings available.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of lettings.
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the details of a specific letting.

    Args:
        request: The HTTP request object.
        letting_id: The ID of the letting to display.

    Returns:
        HttpResponse: The rendered HTML page displaying the details of the letting.
    """

    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {'title': letting.title, 'address': letting.address}
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.exception(f"Error loading letting {letting_id}: {e}")
        raise
