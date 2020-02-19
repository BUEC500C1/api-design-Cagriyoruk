from AirportWeatherAPI import *
import pytest

def test_airport():
  city = ['Boston', 'New York']

  for each in city:
    AirportWeatherAPI.get_weather(each)
