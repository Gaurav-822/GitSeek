import requests
import json

name = "Gaurav-822"
url = f'https://api.github.com/users/{name}'
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Decode the JSON response
    data = json.loads(response.content)

    # Print the user's name
    print(data["name"])
else:
    print('Request failed with status code:', response.status_code)
