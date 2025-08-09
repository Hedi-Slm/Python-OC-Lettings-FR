Database Structure and Data Models
==================================

This section describes the SQLite database structure and the Django models used in the OC Lettings Site application.

Database Architecture
---------------------

The application uses SQLite with a simple, effective relational schema. The database is organized around three Django apps:

* ``oc_lettings_site`` — Main application (no specific models)
* ``lettings`` — Models related to rental properties (addresses and lettings)
* ``profiles`` — Models related to user profiles (profiles)

Models in the ``lettings`` app
------------------------------

Address Model
~~~~~~~~~~~~~

The ``Address`` model represents a full physical address.

**Model structure:**

.. code-block:: python

    class Address(models.Model):
        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

**Field details:**

``number`` (PositiveIntegerField)
    Street or building number

    * Type: Positive integer
    * Validation: Maximum 9999
    * Required: Yes

``street`` (CharField)
    Street name, avenue, boulevard, etc.

    * Type: String
    * Max length: 64 characters
    * Required: Yes

``city`` (CharField)
    City name

    * Type: String
    * Max length: 64 characters
    * Required: Yes

``state`` (CharField)
    State or region code (abbreviated)

    * Type: String
    * Length: Exactly 2 characters
    * Validation: Minimum length 2
    * Example: "NY", "CA", "TX"
    * Required: Yes

``zip_code`` (PositiveIntegerField)
    Postal code

    * Type: Positive integer
    * Validation: Maximum 99999
    * Required: Yes

``country_iso_code`` (CharField)
    Country code in ISO format

    * Type: String
    * Length: Exactly 3 characters
    * Validation: Minimum length 3
    * Example: "USA", "CAN", "FRA"
    * Required: Yes


Letting Model
~~~~~~~~~~~~~

The ``Letting`` model represents a rental listing.

**Model structure:**

.. code-block:: python

   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

**Field details:**

``title`` (CharField)
    Descriptive title of the rental listing

    * Type: String
    * Max length: 256 characters
    * Required: Yes

``address`` (OneToOneField)
    Relation to the ``Address`` model

    * Type: OneToOne relation
    * Target model: ``Address``
    * On delete: ``CASCADE``
    * Required: Yes


Models in the ``profiles`` app
------------------------------

Profile Model
~~~~~~~~~~~~~

The ``Profile`` model extends Django's user information.

**Model structure:**

.. code-block:: python

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

**Field details:**

``user`` (OneToOneField)
    Relation to Django's ``User`` model

    * Type: OneToOne relation
    * Target model: ``django.contrib.auth.models.User``
    * On delete: ``CASCADE``
    * Required: Yes

``favorite_city`` (CharField)
    User's favorite city

    * Type: String
    * Max length: 64 characters
    * Optional: ``blank=True``
    * May be empty


Model Relations
---------------


Relationship descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~

**User ↔ Profile**
    OneToOne relation between Django's standard User model and the custom Profile model.

    * Each Django user can have one profile
    * Each profile is linked to exactly one user
    * Cascade delete: deleting a user removes the profile

**Address ↔ Letting**
    OneToOne relation between Address and Letting.

    * Each letting has one address
    * Each address is used by exactly one letting
    * Cascade delete: deleting an address removes the letting

