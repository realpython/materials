# Make a Location-Based Web App With Django and GeoDjango

This folder contains the bonus material & example projects for our [Make a Location-Based Web App With Django and GeoDjango](https://realpython.com/location-based-app-with-geodjango-tutorial) tutorial on Real Python.

Check out [Make a Location-Based Web App With Django and GeoDjango](https://realpython.com/location-based-app-with-geodjango-tutorial/) for more information.

## Requirements

- Python 3.12 or later
- GDAL, GEOS, and PROJ installed on your system
- A PostgreSQL database with the PostGIS extension, for example:

```console
$ docker run --name=postgis -d -e POSTGRES_USER=user001 \
    -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis \
    -p 5432:5432 kartoza/postgis:18-3.6
```

Install the Python dependencies, then load the data and run the server:

```console
$ python -m pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
