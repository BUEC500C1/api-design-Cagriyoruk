import pytest
from AirportWeatherAPI import *

def test_weather():
  assert get_weather('Boston') != ""