from AirportWeatherAPI import *
import pytest

def test_airport():
  a_names = ['Wbz Heliport', 'Total Rf Heliport']
  c_names = ['Boston', 'Bensalem']

  for i in range(len(a_names)):
    assert get_airport(a_names[i]) == c_names[i] 
