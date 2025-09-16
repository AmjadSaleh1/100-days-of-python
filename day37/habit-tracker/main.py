import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "asd132ewaad",
    "username": "amjad123",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_params = {
    "id": "graph1",
    "name": "ReadingGraph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

today = datetime.now().strftime("%Y%m%d")

Update_Graph_Param = {
    "date": today,
    "quantity": input("How many hours did you read today? "),
}

put_in_graph = {
    "quantity": "5"
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# update_g_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=update_g_endpoint, json=Update_Graph_Param, headers=headers)
# print(response.text)

# put_n_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.put(url= put_n_graph_endpoint, json= put_in_graph, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)