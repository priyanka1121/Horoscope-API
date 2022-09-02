from flask import Flask
from decouple import config
from flask_restx import Api
from core import app

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Horoscope API',
    description='Get horoscope data easily using the below APIs',
    license='MIT',
    contact='Priyanka',
    doc='/',
    prefix='/api/v1'
)

