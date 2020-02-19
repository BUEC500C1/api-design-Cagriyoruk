from AirportWeatherAPI import *
import pytest

def test_airport():
  a_names = ['Wbz Heliport', 'Total Rf Heliport']

  for each in a_names:
    get_airport(each)
