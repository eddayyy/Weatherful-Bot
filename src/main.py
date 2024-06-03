# This repository does not hold the entire source code for weatherful bot, it serves to show proof of concept
# Critical code is omitted from this repository
from WeatherfulBot import WeatherfulBot


if __name__ == '__main__':
    weather = WeatherfulBot()
    weather.tweet('sun')
    weather.tweet('weekly')
    weather.tweet('hourly')
