from api import create_app
from config import config_dict
from api.views import CityView, CityListView, WeatherRequestView, HistoryView
from flask_restful import Api
from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv('ENV')

config = config_dict.get(environment)

app = create_app(config) #config=config_dict['production']


if __name__ == "__main__":
    app.run()

# migrate
#db.create_all()

# >>> import secrets
# >>> secrets.token_hex(12)

#test
#pytest

#flask shell
