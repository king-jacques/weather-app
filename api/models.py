from api.exceptions import APIException
from api.utils import db
from .utils import BaseModel
import requests
from config import OPEN_WEATHER_ENDPOINT
import json
from .enums import Status

class City(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def get_weather_report(self):
        endpoint = OPEN_WEATHER_ENDPOINT.format(city=self.name)
        try:
            response = requests.get(endpoint)
        except Exception as e:
            raise APIException(f"An Error Occured. {str(e)}")
        return response

    def __str__(self):
        return f"{self.name}"
    
class WeatherRequestLog(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    data = db.Column(db.Text, nullable=False)
    # city = db.relationship('City', backref='logs')
    # city_pk = db.Column(db.Integer, nullable=False)

    @property
    def timestamp(self):
        return self.created
    
    @property
    def summary(self):
        from .serializers import weather_summary
        data = json.loads(self.data)
        if self.status == Status.SUCCESS.value:
            
            main = data["main"]
            weather = data["weather"][0]
            main_summary = {key: value for key, value in main.items() if key in weather_summary}
            weather_sum = {key: value for key, value in weather.items() if key in weather_summary}
            summary = main_summary | weather_sum
        else:
            summary = data
        return summary
    
    @property
    def city_name(self):
        return City.query.get(self.city_id)
    
    @classmethod
    def log(cls, data, city_id, status):
        cls.create(data=data, city_id=city_id, status=status)