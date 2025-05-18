import requests
from datetime import datetime

USERNAME = "pixela_username"
TOKEN = "pixela_token"
GRAPH_ID = "graph1"
DATE = datetime(year=2025, month=5, day=17)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Time",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response  = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


#print(DATE.strftime("%Y%m%d"))

pixel_config = {
    "date" : DATE.strftime("%Y%m%d"),
    "quantity" : "1.0",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{DATE.strftime('%Y%m%d')}"

new_update_data = {
    "quantity": "0.5"
}

# response = requests.put(url=update_endpoint, json=new_update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{DATE.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
