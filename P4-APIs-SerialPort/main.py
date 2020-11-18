# importing the requests library 
import requests  # pip install requests
import json
import serial # python -m pip install pyserial
import serial.tools.list_ports
import time

from errors import *

def main():
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

    # get user input to customize the API request
    zipcode = input("Enter your zip code to get the weather: ")
    print(zipcode)
    print(type(zipcode))

    # once we have the port to use and zipcode, 
    # we will do an API request every x minutes and then 
    # send the weather data obtained from the API to the selected port.
    i=0
    while True: 
        # Indicate what iteration we're on
        i += 1
        print(i)

        # Get the weather data via the API
        # insert user input into api call https://matthew-brett.github.io/teaching/string_formatting.html
        # URL = "api.openweathermap.org/data/2.5/weather"
        resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=e28b09913aed610ae9e48d01fbb747a8".format(zipcode))
        if resp.status_code != 200:
            raise APIError(resp.status_code)
        # save json response into data 
        data = resp.json() 

        # Print entire API response for debug
        #print(json.dumps(data, indent=4))

        # Get temperature data from the response
        tempK = data["main"]["temp"]
        tempF = round(((9/5) * tempK) - 459.67,2)
        # (1) Round to nearest integer (nearest even int for "tie"),
        # (2) convert to int (remove ".0"),
        # (3) convert to string for transmission over serial
        tempFstr = str(int(round(tempF,0)))

        # Print the time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)

        # Print the relevant weather data
        weatherDesc =  "Description " + data["weather"][0]["description"]
        weatherTemp =  "Temperature "  + str(data["main"]["temp"])
        weatherIconNum = data["weather"][0]["icon"]
        print(weatherDesc)
        print(weatherIconNum)
        print( "Temperature in K:" + str(tempK))
        print( "Temperature in F:" + str(tempF))

        # Send the icon code to the Arduino
        #==> use these codes: https://openweathermap.org/weather-conditions
        myPort.write(weatherIconNum.encode())
        myPort.write(tempFstr.encode())

        # Test read the serial port, using a wire to loopback TX into RX on the port.
        # clear from prev iterations
        readvar = None
        # a small wait, to let the port buffer the data
        time.sleep(0.1)
        readvar = myPort.read_all()
        print(readvar)
        
        # Wait until next request
        # for testing purposes, we will send the request every 5 seconds
        time.sleep(5)



main()