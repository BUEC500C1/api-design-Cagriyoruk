from AirportWeatherAPI import *

def test_airport():
	assert get_airport("Wbz Heliport") == "Boston"
