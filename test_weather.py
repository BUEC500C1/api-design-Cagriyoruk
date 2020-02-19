from AirportWeatherAPI import *
import pytest

def test_airport():
  city = ['Boston', 'New York']

  for each in city:
    weather_try.get_weather(each)
