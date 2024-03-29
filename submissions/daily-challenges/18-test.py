import requests

# GET request
apiURL = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "User-Agent": "MyApp/1.0" 
}

GETres = requests.get(apiURL, headers=headers)

print(f"GET response: {GETres.status_code}")
print("\nResponse Headers:")
for key, value in GETres.headers.items():
    print(f"{key}: {value}")
print("\nResponse Content:", GETres.text)

# POST request
data = {
    "title": "hatdog",
    "body": "zb1" 
}

POSTres = requests.post(apiURL, json=data, headers=headers)

print(f"\nPOST response: {POSTres.status_code}")
print("\nResponse Headers:")
for key, value in POSTres.headers.items():
    print(f"{key}: {value}")
print("\nResponse Content:", POSTres.text)