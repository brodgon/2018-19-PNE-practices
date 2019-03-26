import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="
METHOD = "GET"

city = input("Please, introduce a city: ")

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}


conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + city, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

print("Chosen city: ", weather[0]['title'])
print("Location type: ", weather[0]['location_type'])
print("Where on Earth ID: ", weather[0]['woeid'])
print("Latitude long: ", weather[0]['latt_long'])
woeid = str(weather[0]['woeid'])

"""--------"""


# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + woeid + '/', None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)

time = weather['time']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']

print()

print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))

