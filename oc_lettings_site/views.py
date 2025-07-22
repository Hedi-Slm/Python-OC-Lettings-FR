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
