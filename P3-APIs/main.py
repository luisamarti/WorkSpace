# importing the requests library 
import requests  # pip install requests
import json

from errors import *


# api-endpoint 
#URL = "api.openweathermap.org/data/2.5/weather"
resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=e28b09913aed610ae9e48d01fbb747a8")
if resp.status_code != 200:
    raise APIError(resp.status_code)

#save json response into data 
data = resp.json() 
#print(data)
# try parsing data - how do you view or extract a prop
print(json.dumps(data, indent=4))
weatherDesc =  "Description " + data["weather"][0]["description"]
weatherTemp =  "Temperature "  + str(data["main"]["temp"])
tempK = data["main"]["temp"]
tempF =  round(((9/5) * tempK) - 459.67,2)
print(weatherDesc)
print(tempK)
print( "weather Temp F " + str(tempF))