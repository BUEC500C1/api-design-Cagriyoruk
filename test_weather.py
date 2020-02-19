from AirportWeatherAPI import *

def test_weather():
  city = ['Boston', 'New York']

  for each in city:
    get_weather(each)
