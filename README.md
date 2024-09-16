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