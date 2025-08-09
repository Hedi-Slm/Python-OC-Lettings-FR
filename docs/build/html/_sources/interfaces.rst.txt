Programming Interfaces
======================

This section describes the programming interfaces of the OC Lettings Site application, based on Django's MVT (Model-View-Template) architecture.

View Architecture
-----------------

The application primarily uses Django function-based views to serve web pages. No REST API is implemented in this version of the application.

URL Configuration
-----------------

Main URLs (oc_lettings_site)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File:** ``oc_lettings_site/urls.py``

.. code-block:: python

    urlpatterns = [
        path('', views.index, name='index'),
        path('lettings/', include('lettings.urls')),
        path('profiles/', include('profiles.urls')),
        path('admin/', admin.site.urls),
    ]

**Available URLs:**

* ``/`` — Main home page
* ``/lettings/`` — Includes URLs from the lettings app
* ``/profiles/`` — Includes URLs from the profiles app
* ``/admin/`` — Django admin interface

Lettings app URLs
~~~~~~~~~~~~~~~~~

**File:** ``lettings/urls.py``

.. code-block:: python

    app_name = 'lettings'

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:letting_id>/', views.letting, name='letting'),
    ]

**Namespaced URLs:**

* ``/lettings/`` → ``lettings:index`` — Listing of lettings
* ``/lettings/<int:letting_id>/`` → ``lettings:letting`` — Letting detail

Profiles app URLs
~~~~~~~~~~~~~~~~~

**File:** ``profiles/urls.py``

.. code-block:: python

    app_name = 'profiles'

    urlpatterns = [
        path('', views.index, name='index'),
        path('<str:username>/', views.profile, name='profile'),
    ]

**Namespaced URLs:**

* ``/profiles/`` → ``profiles:index`` — List of profiles
* ``/profiles/<str:username>/`` → ``profiles:profile`` — Profile detail

Main app views
--------------

oc_lettings_site/views.py
~~~~~~~~~~~~~~~~~~~~~~~~~

**Index view (Home page)**

.. code-block:: python

   def index(request):

       return render(request, 'index.html')

**Associated template:** ``templates/index.html``

**Purpose:** Home page with navigation to other sections

Lettings app views
------------------

lettings/views.py
~~~~~~~~~~~~~~~~~

**Index view (Lettings list)**

.. code-block:: python

    def index(request):

        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)

**Letting view (Letting detail)**

.. code-block:: python

    def letting(request, letting_id):

        letting = get_object_or_404(Letting, id=letting_id)
        context = {'title': letting.title, 'address': letting.address}
        return render(request, 'lettings/letting.html', context)



**Associated templates:**

* ``lettings/templates/lettings/index.html`` — Lettings list
* ``lettings/templates/lettings/letting.html`` — Letting detail

Profiles app views
------------------

profiles/views.py
~~~~~~~~~~~~~~~~~

**Index view (Profiles list)**

.. code-block:: python

    def index(request):
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)

**Profile view (Profile detail)**

.. code-block:: python

    def profile(request, username):

        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)


**Associated templates:**

* ``profiles/templates/profiles/index.html`` — Profiles list
* ``profiles/templates/profiles/profile.html`` — Profile detail

Error Handling
--------------

Custom error pages
~~~~~~~~~~~~~~~~~~

The application handles common HTTP errors with custom pages.

**404 - Page not found**

.. code-block:: python

   # In oc_lettings_site/views.py
   def handler404(request, exception):

       return render(request, '404.html', status=404)

**500 - Server error**

.. code-block:: python

   # In oc_lettings_site/views.py
   def handler500(request):

       return render(request, '500.html', status=500)

**Configuration in urls.py:**

.. code-block:: python

   # Error handler configuration
   handler404 = 'oc_lettings_site.views.handler404'
   handler500 = 'oc_lettings_site.views.handler500'


Admin Interface
---------------

Django Admin configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The app uses Django's built-in admin interface for data management.

We are using a minimal set of features for this version of the application.
``oc_lettings_site/admin.py`` configuration:

.. code-block:: python

    from django.contrib import admin
    from lettings.models import Letting
    from lettings.models import Address
    from profiles.models import Profile


    admin.site.register(Letting)
    admin.site.register(Address)
    admin.site.register(Profile)

Admin features
~~~~~~~~~~~~~~

Possible features that can be use in Django Admin interface:

* Paginated lists
* Keyword search
* Sidebar filters
* Bulk edit actions
* Full CRUD interface
