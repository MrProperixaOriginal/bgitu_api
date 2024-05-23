import requests
import json
import time

api_link = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(api_link)
if response.status_code == 200:
    print(json.loads(response.text)["setup"])
    time.sleep(2)
    print(json.loads(response.text)["punchline"])
else:
    print(response.status_code)
