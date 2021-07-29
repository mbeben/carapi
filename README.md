carapi
========================

Dependencies
------------

-   Python 3.9 and [pipenv](http://pipenv.readthedocs.io/en/latest/)
-   Optional: [Docker](https://docs.docker.com/get-started/),
    [Docker Compose](https://docs.docker.com/compose/install/) and if you want to use docker.
    
Installation and commissioning
------------------------------

1.  Clone the project :

        git clone https://github.com/mbeben/carapi.git
        cd carapi

2.  Prepare python environment :

        pipenv install -r requirements.txt
        pipenv shell
        # Click Ctrl-D to exit virtualenv.

3.  Create database :

        python manage.py migrate
        # Optionally create super user to get access to admin page
        python manage.py createsuperuser

Docker
------------------------------

To use docker for development go to the project root and use:
        
        docker-compose build

After it was built use this command to start the server
        
        docker-compose up

The API will start at http://0.0.0.0:8000/