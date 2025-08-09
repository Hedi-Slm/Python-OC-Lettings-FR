Usage Guide
===========

This section describes the main use cases of the OC Lettings Site application, with practical examples for each user type.

User Types
----------

The application targets three main user types:

**Any visitors**
    Can browse public lettings and profiles.

**Administrators**
    Have access to the admin interface to manage content.

Primary Use Cases
-----------------

1. Browsing rental listings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Allow users to discover available rental properties

**Steps:**

1. **Open home page**

   * URL: ``http://localhost:8000/`` or website url
   * Action: Home page shows navigation links

2. **Go to lettings**

   * Click the "Lettings" link
   * Destination URL: ``http://localhost:8000/lettings/``

3. **View the list**

   * All available lettings are displayed
   * Each letting shows a title
   * Clickable links lead to detail pages

4. **View letting details**

   * Click a specific letting
   * URL: ``http://localhost:8000/lettings/<id>/``
   * Display: Full title and detailed address

**Navigation example:**

.. code-block:: text

   Home → Lettings → Lettings list → Letting detail


2. Browsing user profiles
~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Allow discovery of user profiles on the platform

**Steps:**

1. **From the home page**

   * Click the "Profiles" link
   * Destination URL: ``http://localhost:8000/profiles/``

2. **View the profiles list**

   * All user profiles are listed
   * Usernames are links

3. **View profile detail**

   * Click a username
   * URL: ``http://localhost:8000/profiles/<username>/``
   * Display: Profile information

**Navigation example:**

.. code-block:: text

   Home → Profiles → Profiles list → Profile detail


3. Content administration
~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Full management of application data

**Actors:** Administrators only

**Prerequisites:** Superuser account created

**Access steps:**

1. **Log in to admin interface**

   * URL: ``http://localhost:8000/admin/``
   * Enter admin credentials
   * Authenticate to access the dashboard

2. **Navigate the admin**

   * Main dashboard with available sections

Address management:

* **Addresses list:**
  * Display: number, street, city, state, zip code
  * Actions: Add, edit, delete

* **Create/edit address:**
  * Form with field validations
  * Constraints: number (max 9999), state (2 chars), etc.
  * Save with integrity checks

Lettings management:

* **Lettings list:**
  * Display: title and associated address
  * Actions: Add, edit, delete

* **Create/edit letting:**
  * Select an existing address (OneToOne relation)
  * Enter title (max 256 characters)
  * Validate relations

Profiles management:

* **Profiles list:**
  * Display: user and favorite city
  * Actions: Add, edit, delete

* **Create/edit profile:**
  * Associate with an existing Django user
  * Favorite city optional

User management:

* Standard Django interface for:
  * Creating user accounts
  * Managing permissions and groups
  * Activating/deactivating users
  * Resetting passwords