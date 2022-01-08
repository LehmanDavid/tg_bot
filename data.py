import requests
from datetime import datetime
import json
response_API = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/USD/{}/'.format(datetime.date(datetime.now())))

data = response_API.text
parse_json = json.loads(data)
course = parse_json[0]["Rate"]
value = 'The dollar rate is {} soums'.format(course)

