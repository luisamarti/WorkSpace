# importing the requests library 
import requests 
import json

# api-endpoint 
#URL = "api.openweathermap.org/data/2.5/weather"
resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=e28b09913aed610ae9e48d01fbb747a8")
if resp.status_code == 200:
    raise APIError(resp.status_code)

data = resp.json() 
print(data)


class APIError(Exception):
    """An API Error Exception"""
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)
   