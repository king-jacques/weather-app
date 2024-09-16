ROUTES TO IMPLEMENT

METHOD ROUTE FUNCTIONALITY


# Weather API with Open Weather App

 

## How to run the project

Clone the project Repository
```
git clone https://github.com/king-jacques/weather-app.git

```

Enter the project folder and create a virtual environment
``` 
$ cd weather_app

$ python -m venv env 

```

Activate the virtual environment
``` 
$ source env/bin/actvate #On linux Or Unix

$ source env/Scripts/activate #On Windows 
 
```

Install all requirements

```
$ pip install -r requirements.txt
```

Run the project in development
```
$ export FLASK_APP=api/

$ export FLASK_DEBUG=True

$ export OPEN_WEATHER_API_KEY=Your_API_KEY
```

# RUN MIGRATIONS
Since i am using a local sqlite db. you need to run the db migrations the first time
```
$ flask shell
$ db.create_all()
from setup import load_cities
load_cities()
exit()
```


# Finally

To run the server.

```
$ python runserver.py

```
Or 
``` 
$ flask run
```

## How to Test project

After successfully running project, to test:
```
$ pytest
```

** I have only implemented basic tests for the history and weather endpoints.

# Potential Improvements
- production grade db with postgres
- better error logging using a logger
- better error handling
- more robust unit tests
- containerize app with docker


# API Documentation
Swagger documentation available at localhost:5000/docs