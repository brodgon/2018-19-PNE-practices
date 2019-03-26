import http.client
import json

HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random","/jokes/count","/categories"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)


for i in range(len(ENDPOINT)):
    conn.request(METHOD, ENDPOINT[i], None, headers)

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    joke = json.loads(text_json)

    if i ==0:
        print("Random Chuck Norris Joke: ", "\n","\t" ,joke['value']['joke'])
    elif i == 1:
        print("Total number of jokes available is:" , joke['value'])
    else:
        print("The {} categories found are: {}".format(len(joke['value']),joke['value']))


