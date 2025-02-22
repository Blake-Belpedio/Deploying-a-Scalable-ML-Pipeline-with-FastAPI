import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = 'http://127.0.0.1:8000'
response = requests.get(r)

# TODO: print the status code
print('Get Request:')
print("Status Code:", response.status_code)
# TODO: print the welcome message
print("Response:", response.json())
print()



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
r = "http://127.0.0.1:8000/data/"
res_p = requests.post(r, json=data)

print('Post Request')
# TODO: print the status code
print("Status Code:", res_p.status_code)

# TODO: print the result
print("Response:", res_p.json())