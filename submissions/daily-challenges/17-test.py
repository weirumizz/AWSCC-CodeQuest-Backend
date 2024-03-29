#https://jsonplaceholder.typicode.com/
import requests

baseURL = "https://jsonplaceholder.typicode.com/"

resPATH = "/users"

fullURL = baseURL + resPATH

response = requests.get(fullURL)
print(f"GET response: {response}")

if response.status_code == 200:
    print("Request successful!")
else: 
    print("Request failed!")


