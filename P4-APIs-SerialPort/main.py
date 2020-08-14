# importing the requests library 
import requests  # pip install requests
import json
import serial # python -m pip install pyserial
import serial.tools.list_ports
import time


from errors import *

comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)

myPort = None  
i = 1;
for element in connected:
    print(str(i) + ": " + element)
    i+=1

#pull user input
portToOpen = input("Pick a port number from the list: ")

# Need bounds checking for user input to array connected

try:
    #myPort will store the port to use 
    myPort = serial.Serial(connected[int(portToOpen)-1])
#check if an error was return 
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    

print( myPort )

#exit()

# get user input to customize the API request
zipcode = input("Enter your zip code to get the weather: ")
print(zipcode)
print(type(zipcode))


# once we have the port to use and zipcode, we will do an API request every x minutes and then send the weather data obtained from the API to the selected
# port. This will check if is new data


# api-endpoint 
# insert user input into api call https://matthew-brett.github.io/teaching/string_formatting.html
#URL = "api.openweathermap.org/data/2.5/weather"
i=0
while True: 
    resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=e28b09913aed610ae9e48d01fbb747a8".format(zipcode))
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
    #for testing purposes, we will send the request every 5 seconds
    i += 1
    print(i)
    time.sleep(10)