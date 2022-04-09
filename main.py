import requests


CITY = "Douala"
MY_LAT = 4.051056
MY_LNG = 9.767869

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG
}
response_sunrise = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
print(response_sunrise.json())
