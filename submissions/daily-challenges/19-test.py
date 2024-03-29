# https://api.spacexdata.com/v5/launches/latest
import requests

apiURL = "https://api.spacexdata.com/v5/launches/latest"

headers = {
    "User-Agent": "My-Req/01"
}

GETres = requests.get(apiURL, headers=headers)

if GETres.status_code == 200:
    print("Request successful!")
    print(f"\nGET response: {GETres.status_code}")
    data = GETres.json()
    name = data["name"]
    date_utc = data["date_utc"]
    success = data["success"]
    details = data["details"]

    print(f"\nName: {name}")
    print(f"Date Released: {date_utc}")
    print(f"Success: {'Yes' if success else 'No'}")
    print(f"Details: {details}")
else: 
    print("Request failed!")
    print(f"\nError Code: {GETres.status_code}")