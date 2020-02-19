import pytest
from AirportWeatherAPI import *

def test_weather():
	get_weather('Boston')
	get_airport('Wbz Heliport')