from django.shortcuts import render


def index(request):
    """
    Renders the index page (home page).

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page.
    """
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """
    Custom 404 error page handler.

    Args:
        request: The HTTP request object.
        exception: The exception that caused the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page.
    """

    return render(request, 'error_404.html', status=404)


def custom_500_view(request):
    """
    Custom 500 error page handler.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 500 error page.
    """

    return render(request, 'error_500.html', status=500)
