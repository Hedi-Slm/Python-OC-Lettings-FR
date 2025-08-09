Deployment Procedures and Application Management
================================================

This section details the deployment architecture, automated procedures, and management of the OC Lettings Site application in production.

Deployment Architecture
-----------------------

Overview of the CI/CD Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application uses a modern deployment architecture based on:

* **GitHub** - Source code repository and workflow triggering
* **GitHub Actions** - Automated CI/CD pipeline
* **Docker Hub** - Container registry
* **Render** - Cloud hosting platform


GitHub Actions Workflow
-----------------------

Pipeline Configuration
~~~~~~~~~~~~~~~~~~~~~~

**File:** ``.github/workflows/CI-CD.yml``

The pipeline consists of three main jobs executed sequentially:

1. **Testing and validation** (on all branches)
2. **Containerization** (on the master branch only)
3. **Deployment** (on the master branch only)

Job 1: Testing and Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Trigger:** Push or Pull Request on any branch

**Steps:**

.. code-block:: yaml

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Collect static files
        run: python manage.py collectstatic --noinput

      - name: Run lint
        run: flake8 .

      - name: Run tests with coverage
        run: pytest --cov --cov-fail-under=80

**Success Criteria:**

* No flake8 linting errors
* All pytest tests pass
* Code coverage ≥ 80%

Job 2: Containerization
~~~~~~~~~~~~~~~~~~~~~~~

**Trigger:** Success of the testing job AND master branch

**Steps:**

.. code-block:: yaml

  build:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.build.outputs.tag }}

    steps:
      - uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_PASSWORD }}

      - name: Build and tag Docker image
        id: build
        run: |
          TAG=${{ github.sha }}
          echo "tag=$TAG" >> $GITHUB_OUTPUT
          docker build -t ${{ env.DOCKER_IMAGE }}:$TAG -t ${{ env.DOCKER_IMAGE }}:latest .

      - name: Push Docker image
        run: |
          docker push ${{ env.DOCKER_IMAGE }}:${{ steps.build.outputs.tag }}
          docker push ${{ env.DOCKER_IMAGE }}:latest

**Results:**

* Docker image built and tested
* Push to Docker Hub with two tags:

  * ``latest`` - Latest stable version
  * ``<commit-sha>`` - Commit-specific version

Job 3: Deployment
~~~~~~~~~~~~~~~~~

**Trigger:** Success of the containerization job

**Steps:**

.. code-block:: yaml

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest

    steps:
      - name: Trigger Render deployment
        run: |
          curl -X POST "${{ secrets.RENDER_DEPLOY_HOOK }}"

**Operation:**

* Call the Render deployment webhook
* Render automatically pulls the new image
* Automatic service restart

Variables and Secrets Configuration
-----------------------------------

GitHub Actions Variables
~~~~~~~~~~~~~~~~~~~~~~~~

**Repository Variables (public):**

Variables are defined in the repository settings in GitHub.

.. code-block:: bash

   # Environment variables for production
   DJANGO_ALLOWED_HOSTS_PROD="localhost"
   DJANGO_DEBUG_PROD="False"
   DJANGO_MIDDLEWARE_PROD="django.middleware.security.SecurityMiddleware,..."
   DJANGO_STATICFILES_STORAGE_PROD="whitenoise.storage.CompressedManifestStaticFilesStorage"

   # Docker image
   DOCKERHUB_IMAGE="hedislm/letting_docker"

**Repository Secrets (private):**

.. code-block:: bash

   # Docker Hub authentication
   DOCKERHUB_USERNAME="your_dockerhub_username"
   DOCKERHUB_PASSWORD="your_dockerhub_password"

   # Django configuration
   DJANGO_SECRET_KEY="your_django_secret_key"

   # Monitoring
   SENTRY_DSN="your_sentry_dsn"

   # Render deployment
   RENDER_DEPLOY_HOOK="your_render_deployment_hook"

Render Configuration
~~~~~~~~~~~~~~~~~~~~

**Render Environment Variables:**

.. code-block:: bash

   # Django production configuration
   DJANGO_ALLOWED_HOSTS="your-domain.onrender.com"
   DJANGO_DEBUG="False"
   DJANGO_SECRET_KEY="your_secret_key"
   DJANGO_MIDDLEWARE="django.middleware.security.SecurityMiddleware,..."
   DJANGO_STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

   # Monitoring and observability
   SENTRY_DSN="your_sentry_dsn"

**Render Service Configuration:**

* **Service type:** Web Service
* **Source:** Docker
* **Docker image:** ``hedislm/letting_docker:latest``
* **Port:** 8000
* **Start command:** Automatic (defined in Dockerfile)
* **Auto-deploy:** Enabled with webhook

Docker Containerization
-----------------------

Dockerfile Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

**Optimized Dockerfile:**

.. code-block:: dockerfile

    FROM python:3.11-slim

    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1

    # Set work directory
    WORKDIR /app

    # Install system dependencies
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

    # Install Python dependencies
    COPY requirements.txt .
    RUN pip install --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt

    # Copy project files
    COPY . .

    # Collect static files and start server
    CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]

**Applied optimizations:**

* Lightweight base image (``python:3.11-slim``)
* Static files collected at build time
* Gunicorn command optimized for production

.dockerignore File
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    __pycache__/
    *.pyc
    *.pyo
    *.pyd
    venv/
    .env

Docker Image Management
~~~~~~~~~~~~~~~~~~~~~~~

**Tagging strategy:**

* ``latest`` - Last version deployed in production
* ``<commit-sha>`` - Specific version for rollback

.. note::

   * If you want to run a container locally check:
   * :doc:`installation`
   * :doc:`quickstart`

Deployment Validation
---------------------

Once code is pushed to GitHub, you will be able to check in real time the status of the deployment in the **Actions** tab.
Inside this tab you will also be able to view the logs of the deployment and details for each job that has been executed by the pipeline.
We will also be able access different metrics to monitor the performance of the pipeline.