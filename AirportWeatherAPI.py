# Cagri Yoruk cyoruk@bu.edu
# Airport Weahter API
import requests
from datapackage import Package

def get_airport(a_names):
  airport_name = a_names
  package = Package('https://datahub.io/core/airport-codes/datapackage.json')
  # print processed tabular data (if exists any)
  for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
      airport_list = resource.read()
      for each in airport_list:
        every = each[2]
        if every == airport_name:
          city = each[7]
          break
  get_weather(city)

def get_weather(city):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=("YOUR API KEY GOES HERE")'.format(city)
    res = requests.get(url)
    data = res.json()
    condition = data['weather'][0]['description']
    max_temp = data['main']['temp_max']
    min_temp = data['main']['temp_min']
    print("The weather is {} , the max temperature is {} and the minimum temperature is {}".format(condition, max_temp, min_temp))
