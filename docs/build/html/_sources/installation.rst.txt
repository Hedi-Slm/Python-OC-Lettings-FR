Installation Instructions
=========================

Prerequisites
-------------

Before installing the application, make sure you have the following installed on your system:

* **Python 3.8+** - Main programming language
* **Git** - Version control system
* **Docker** (optional) - For containerization
* **A code editor** - VS Code, PyCharm, or others

Local Installation
------------------

Step 1: Clone the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/Hedi-Slm/Python-OC-Lettings-FR
   cd /path/to/Python-OC-Lettings-FR

Step 2: Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Linux/Mac:**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

**Windows:**

.. code-block:: bash

   python -m venv venv
   venv\Scripts\activate

Step 3: Install dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install -r requirements.txt

Step 4: Configure environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a ``.env`` file at the project root with the following content:

.. code-block:: bash

   SENTRY_DSN=your_sentry_dsn_here
   DJANGO_SECRET_KEY=your_secret_key_here
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=["localhost"]
   DJANGO_MIDDLEWARE=["django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware", "django.middleware.clickjacking.XFrameOptionsMiddleware"]
   DJANGO_STATICFILES_STORAGE=django.contrib.staticfiles.storage.StaticFilesStorage

.. warning::

   Never commit the ``.env`` file to Git. It contains sensitive information.


Detailed Environment Variables
-------------------------------

SENTRY_DSN
~~~~~~~~~~

Sentry configuration URL for error monitoring.

* **Development**: Optional (leave empty to disable)
* **Production**: Required

DJANGO_SECRET_KEY
~~~~~~~~~~~~~~~~~

Django secret key for cryptographic security.

* **Generation**: ``python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'``
* **Format**: 50-character alphanumeric string

DJANGO_DEBUG
~~~~~~~~~~~~

Django debug mode.

* **Development**: ``True``
* **Production**: ``False``

DJANGO_ALLOWED_HOSTS
~~~~~~~~~~~~~~~~~~~~

List of domains allowed to serve the application.

* **Development**: ``localhost,127.0.0.1``
* **Production**: Your production domain

DJANGO_MIDDLEWARE
~~~~~~~~~~~~~~~~~

List of Django middlewares to use. The default configuration includes:
'whitenoise.middleware.WhiteNoiseMiddleware' is needed when using whitenoise as a static file server

DJANGO_STATICFILES_STORAGE
~~~~~~~~~~~~~~~~~~~~~~~~~~

Static file storage system.

* **Development**: ``django.contrib.staticfiles.storage.StaticFilesStorage``
* **Production**: ``whitenoise.storage.CompressedManifestStaticFilesStorage``

Installation Verification
-------------------------

Once installed, you can verify everything works:

.. code-block:: bash

   # Run the development server
   python manage.py runserver

   # Run tests
   pytest

   # Check linting
   flake8

The application should be accessible at: http://localhost:8000

Docker Installation
-------------------

Alternative for quick setup with Docker:

Step 1: Pull the image
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker pull hedislm/letting_docker:latest

Step 2: Run the container
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run -d -p 8000:8000 ^
     -e "DJANGO_SECRET_KEY=your_secret_key" ^
     -e "DJANGO_DEBUG=False" ^
     -e "DJANGO_ALLOWED_HOSTS=[\"localhost\",\"127.0.0.1\"]" ^
     -e "DJANGO_MIDDLEWARE=[\"django.middleware.security.SecurityMiddleware\",\"django.contrib.sessions.middleware.SessionMiddleware\",\"django.middleware.common.CommonMiddleware\",\"django.middleware.csrf.CsrfViewMiddleware\",\"django.contrib.auth.middleware.AuthenticationMiddleware\",\"django.contrib.messages.middleware.MessageMiddleware\",\"django.middleware.clickjacking.XFrameOptionsMiddleware\",\"whitenoise.middleware.WhiteNoiseMiddleware\"]" ^
     -e "DJANGO_STATICFILES_STORAGE=whitenoise.storage.CompressedManifestStaticFilesStorage" ^
     -e "SENTRY_DSN=your_sentry_dsn" ^
     hedislm/letting_docker:latest
