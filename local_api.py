import json

import requests


r = requests.get('http://127.0.0.1:8000')

print(f'Status Code: {r.status_code}')
print(f'Welcome Message: {r.text}')



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r1 = requests.post('http://127.0.0.1:8000/data/',json = data)

print(f'Status Code: {r1.status_code}')
print(f'Result: {r1.text}')
