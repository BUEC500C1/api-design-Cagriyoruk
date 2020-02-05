# Weather for Airport api-design-Cagriyoruk
api-design-Cagriyoruk created by GitHub Classroom

For all USA Airports, Develop an API and module where we can get current weather conditions for the airport asked by the API.

I created 2 functions in order to get the current weather conditions for the airport location. With first function get_airport, I get the airport location and with that I use it in the second function get_weather to get the current weather condition for the airport location. Then I output the information.

# Preparation
Clone my repository:

``` 
git clone https://github.com/BUEC500C1/api-design-Cagriyoruk
```
 
import my module to your your code

``` 
import AirportWeatherAPI.py
```
## Register to OpenWeatherMap
Regsiter to Openweather Map API to get a key. You need to use it to access the weather conditions. 

Here is an example where you can put your API key.

```
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=("YOUR API KEY GOES HERE")'.format(get_airpot()) 
```

## Example
Enter the Airport name to get the current weather conditions. 

* Run the File
* Enter a valid airport name
* That's all you need to do

![Screenshot_2020-02-04_20-16-28](https://user-images.githubusercontent.com/55101879/73802433-9c81cd00-478b-11ea-9c1a-2d1dd0b92c9c.png)
