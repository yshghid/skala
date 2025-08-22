import requests
import json

url = "http://127.0.0.1:5002/invocations"

# Load input JSON
with open("input.json", "r") as f:
    data = json.load(f)

# Send POST request
response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

# Print prediction result
print(response.json())