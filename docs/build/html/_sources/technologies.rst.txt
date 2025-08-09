Technologies and Programming Languages
======================================

This section lists the technologies, frameworks and tools used in the OC Lettings Site project.

Main Technical Stack
--------------------

Backend
~~~~~~~

**Python 3.8+**
    The project's main programming language.

**Django 4.x**
    High-level Python web framework.

    * MVT (Model-View-Template) architecture
    * Built-in ORM for database management
    * Automatic admin interface
    * Authentication and authorization system
    * Built-in CSRF protection

Database
~~~~~~~~

**SQLite**
    Lightweight relational database included with Django.

    * Ideal for development and small-to-medium applications
    * No server configuration required
    * Single file: ``oc-lettings-site.sqlite3``
    * Django migrations supported

Web Server and Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~

**Gunicorn**
    Python WSGI server for production.

    * High-performance HTTP/WSGI server
    * Compatible with Django applications
    * Worker process management
    * Production-ready configuration

**WhiteNoise**
    Middleware for serving static files.

    * Serves static files without a separate web server
    * Recommended storage: ``whitenoise.storage.CompressedManifestStaticFilesStorage``

Monitoring and Observability
---------------------------

**Sentry**
    Error monitoring and performance platform.

    * Automatic capture of errors and exceptions
    * Performance monitoring
    * Real-time alerts
    * Dashboard for error analysis


Testing and Code Quality
------------------------

Testing Frameworks
~~~~~~~~~~~~~~~~~~

**pytest**
    Modern, powerful testing framework for Python.

    * Simple and expressive syntax
    * Fixtures for test data management
    * Plugin ecosystem
    * Detailed failure reports

**pytest-cov**
    pytest plugin for measuring code coverage.

    * Integrates with coverage.py
    * Configurable coverage threshold (>80%)
    * Interactive HTML reports

Linting and Formatting
~~~~~~~~~~~~~~~~~~~~~~

**flake8**
    Python linting tool for style checks.

    * Enforces PEP 8 standards
    * Detects syntax errors
    * Customizable via ``setup.cfg``
    * Integrated into CI/CD pipeline


DevOps and Deployment
---------------------

Containerization
~~~~~~~~~~~~~~~~

**Docker**
    Container platform for packaging the application.

    * Image based on official Python image
    * Configuration via environment variables
    * Full dependency isolation


**Docker Hub**
    Container registry for storing Docker images.

    * Repository: ``hedislm/letting_docker``
    * Automatic tagging with commit hash

CI/CD
~~~~~

**GitHub Actions**
    Continuous integration and deployment platform.

    * Automated workflows
    * Automated tests and linting
    * Build and push Docker images
    * Automatic deployment to Render


Hosting
~~~~~~~

**Render**
    Modern cloud platform for hosting web applications.

    * Automatic deployment from GitHub
    * Native Docker support
    * Secure environment variables

Developer Tools
---------------

Dependency Management
~~~~~~~~~~~~~~~~~~~~~

**pip**
    Standard Python package manager.

    * Install dependencies from ``requirements.txt``
    * Package version management
    * Virtual environments using ``venv``

Main ``requirements.txt``:

.. code-block:: text

   Django>=4.0,<5.0
   gunicorn>=20.0
   whitenoise>=6.0
   sentry-sdk[django]>=1.0
   pytest>=7.0
   pytest-cov>=4.0
   flake8>=4.0

Version Control
~~~~~~~~~~~~~~~

**Git**
    Distributed version control system.

    * Feature branches
    * Full change history
    * GitHub integration for collaboration
    * Pre-commit hooks for code quality
