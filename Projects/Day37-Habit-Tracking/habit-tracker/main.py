import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "safuw8ru2490woasw35329jjkdf"
USERNAME = "ilyushechka"
GRAPH_ID = "bb83274dsj397"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Pages I've Read Today",
    "unit": "pages",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.today().strftime('%Y%m%d')
pixel_config = {
    "date": today,
    "quantity": input("How many pages did you read today?"),
}

post_response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
print(post_response.text)

# date_to_update = "20220410"
# update_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
#
# day_config = {
#     "quantity": "100"
# }
#
# update_pixel_response = requests.put(url=update_endpoint,headers=headers,json=day_config)
# print(update_pixel_response.text)

# delete_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)
