import pytest
from AirportWeatherAPI import *

def test_weather():
  assert get_airport("Total Rf Helipot") == 'Wrong Input'
  assert get_airport("Total Rf Helport") != None
  assert get_weather("Boston") != None

