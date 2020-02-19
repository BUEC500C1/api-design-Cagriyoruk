import pytest
from AirportWeatherAPI import *

def test_weather():
  assert "message" not in get_weather("Boston")
  assert "message" not in get_weather("New York") 
