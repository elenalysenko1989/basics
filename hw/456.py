import pyowm
import colorama
from colorama import Fore, Back, Style


print(Back.GREEN)
owm = pyowm.OWM('ffce077e8226e68e005114efc4fcf615')
mrg = owm.weather_manager()

place = input("What city/country?: ")

observation = mrg.weather_at_place(place)

w = observation.weather
print(Back.RED)


print("In the city " + place + " now " + w.detailed_status)


