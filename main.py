import datetime
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


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response_sunrise = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response_sunrise.raise_for_status()
data_sunrise = response_sunrise.json()
sunrise = data_sunrise["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_sunrise["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now.hour)
