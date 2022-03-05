import datetime

import pytz
import requests
import time


def look_for_ISS(My_lat, My_lng):
    """Prints "Ayo look" when the ISS is over your head and the sun has set."""
    while True:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        coorinates = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])

        today = datetime.date.today().__str__()

        parameters = {
            "lat": My_lat,
            "lng": My_lng,
            "date": today,
            "formatted": 0
        }
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunset = datetime.datetime.fromisoformat(data["results"]["sunset"])

        if My_lat - 5 < float(coorinates[0]) < My_lat + 5 \
                and My_lng - 5 < float(coorinates[1]) < My_lng + 5 \
                and sunset < datetime.datetime.utcnow().replace(tzinfo=pytz.utc):
            print("Ayo look!")

        time.sleep(30)


if __name__ == "__main__":
    look_for_ISS(float(input("Lat: ")), float(input("Lon:")))
