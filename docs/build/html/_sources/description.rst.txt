Project Description
===================

Overview
--------

OC Lettings Site is a Django web application that allows users to view information about rental properties and user profiles.
The application has been refactored from a monolithic architecture to a modular architecture with three distinct apps to improve maintainability and scalability.

Project Objectives
------------------

The main goal of the project was to modernize an existing application by applying best development practices:

* Refactoring from a monolithic architecture to a modular architecture
* Implementing monitoring and observability
* Setting up an automated CI/CD pipeline
* Improving code quality with tests and linting
* Providing complete technical documentation

Modular Architecture
--------------------

The application is now organized into three distinct modules:

**oc_lettings_site**
    Main application containing the Django configuration, global views.

**lettings**
    Module dedicated to managing rental properties, containing the ``Address`` and ``Letting`` models.

**profiles**
    Module dedicated to managing user profiles, containing the ``Profile`` model.

Main Features
-------------

Rental Listings
~~~~~~~~~~~~~~~

* Display of available rental properties
* View details of a rental (title, full address)
* Intuitive navigation between different listings

Profile Management
~~~~~~~~~~~~~~~~~~

* View the list of user profiles
* Access detailed information for a profile

Admin Interface
~~~~~~~~~~~~~~~

* Integrated Django admin interface
* Full management of users, rentals, and addresses

Monitoring and Observability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Sentry integration for real-time error tracking
* Proper logging in critical code sections
* Custom handling for 404 and 500 errors

Improvements Made
-----------------

Code Quality
~~~~~~~~~~~~

* Fixed all linting errors (flake8)
* Added docstrings to all modules, classes, and functions
* Implemented unit and integration tests
* Achieved over 80% test coverage

Automated Deployment
~~~~~~~~~~~~~~~~~~~~

* CI/CD pipeline using GitHub Actions
* Containerization with Docker
* Automatic deployment on Render
* Optimized static files management

Security
~~~~~~~~

* Environment variables for sensitive data
* Secure configuration for production
* Enabled Django’s security middleware
