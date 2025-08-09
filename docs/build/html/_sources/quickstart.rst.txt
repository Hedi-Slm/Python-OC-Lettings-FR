Quick Start Guide
=================

This section helps you quickly get started with OC Lettings Site after following the installation instructions.

Launching the Application
-------------------------

Development Mode
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Activate virtual environment
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows

   # Start the development server
   python manage.py runserver

The application will be accessible at: ``http://localhost:8000``

Docker Mode
~~~~~~~~~~~

.. code-block:: bash

    docker run -d -p 8000:8000 ^
     -e "DJANGO_SECRET_KEY=your_secret_key" ^
     -e "DJANGO_DEBUG=False" ^
     -e "DJANGO_ALLOWED_HOSTS=[\"localhost\",\"127.0.0.1\"]" ^
     -e "DJANGO_MIDDLEWARE=[\"django.middleware.security.SecurityMiddleware\",\"django.contrib.sessions.middleware.SessionMiddleware\",\"django.middleware.common.CommonMiddleware\",\"django.middleware.csrf.CsrfViewMiddleware\",\"django.contrib.auth.middleware.AuthenticationMiddleware\",\"django.contrib.messages.middleware.MessageMiddleware\",\"django.middleware.clickjacking.XFrameOptionsMiddleware\",\"whitenoise.middleware.WhiteNoiseMiddleware\"]" ^
     -e "DJANGO_STATICFILES_STORAGE=whitenoise.storage.CompressedManifestStaticFilesStorage" ^
     -e "SENTRY_DSN=your_sentry_dsn" ^
     hedislm/letting_docker:latest

Main Pages
----------

Home Page
~~~~~~~~~

* **URL**: ``http://localhost:8000/``
* **Description**: Main page with links to lettings and profiles sections

Rental Listings
~~~~~~~~~~~~~~~

* **URL**: ``http://localhost:8000/lettings/``
* **Description**: Displays all available rental properties
* **Feature**: Click on a listing to view details

Rental Detail
~~~~~~~~~~~~~

* **URL**: ``http://localhost:8000/lettings/<id>/``
* **Description**: Shows detailed information for a rental (title and full address)

Profile List
~~~~~~~~~~~~

* **URL**: ``http://localhost:8000/profiles/``
* **Description**: Shows all user profiles
* **Feature**: Click on a profile to view details

Profile Detail
~~~~~~~~~~~~~~

* **URL**: ``http://localhost:8000/profiles/<username>/``
* **Description**: Shows detailed profile information

Admin Interface
~~~~~~~~~~~~~~~

* **URL**: ``http://localhost:8000/admin/``
* **Description**: Django admin interface
* **Requirement**: Superuser account

.. note::

   To access the admin interface, you must first create a superuser or use the provided credentials:
   username: admin, password: Abc1234!
   .. code-block:: bash

      python manage.py createsuperuser

Essential Development Commands
------------------------------

Unit Tests
~~~~~~~~~~

Run all tests:

.. code-block:: bash

   pytest

Run tests with coverage:

.. code-block:: bash

   pytest --cov=.

Generate HTML coverage report:

.. code-block:: bash

   pytest --cov=. --cov-report=html

Report available at ``htmlcov/index.html``.

Code Linting
~~~~~~~~~~~~

.. code-block:: bash

   flake8

Checks code against PEP8 standards and ``setup.cfg`` configuration.


Application Navigation
----------------------

Typical Workflow
~~~~~~~~~~~~~~~~

1. **Access home page**: ``http://localhost:8000/``
2. **Browse rentals**:
   * Click "Lettings" or go directly to ``/lettings/``
   * Browse the list of rentals
   * Click a rental to see details

3. **Browse profiles**:
   * Click "Profiles" or go directly to ``/profiles/``
   * Browse the list of profiles
   * Click a profile to see details

4. **Admin** (if superuser):
   * Access ``/admin/``
   * Log in
   * Manage users, rentals, and addresses

Default Data Structure
----------------------

Example Rentals
~~~~~~~~~~~~~~~

* Multiple rentals with real addresses
* Descriptive titles
* Full addresses including city, state, and postal code

Example Profiles
~~~~~~~~~~~~~~~~

* User profiles with favorite cities
* Linked to Django user accounts


Development and Customization
-----------------------------

Template Structure
~~~~~~~~~~~~~~~~~~

* ``templates/``: Global templates
* ``templates/lettings/``: Lettings-specific templates
* ``templates/profiles/``: Profiles-specific templates

Static Files
~~~~~~~~~~~~

* ``static/``: CSS, JavaScript, images
* Served by WhiteNoise in production

Logs and Debugging
~~~~~~~~~~~~~~~~~~

In development mode (``DJANGO_DEBUG=True``), errors are displayed directly in the browser with detailed information.

Errors are also sent to Sentry if configured.

Next Steps
----------

Once familiar with the application:

1. **Read the complete documentation** in other sections
2. **Explore the source code** to understand the architecture
3. **Customize the application** to your needs
4. **Deploy to production** following the deployment guide

.. seealso::

   * :doc:`installation` for full installation instructions
   * :doc:`usage` for detailed use cases
   * :doc:`deployment` for production deployment
