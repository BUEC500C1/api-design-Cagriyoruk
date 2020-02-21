import pytest
from AirportWeatherAPI import *

def test_weather():
  assert get_airport(123) == "Wrong Type"
  assert get_airport("Total Rf Helipot") == 'Wrong Input'
  assert get_airport("Total Rf Helport") != None
  assert get_weather(321) == "Wrong Input"
  assert get_weather("Boston") != None
  with pytest.raises(KeyError):
    assert(get_weather('New Yoruk'))
    assert(get_weather('San Zhang'))
    assert(get_weather('Las Brad'))