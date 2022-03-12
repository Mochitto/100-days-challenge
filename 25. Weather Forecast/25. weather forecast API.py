import datetime

import requests


def get_tomorrows_weather(lat, lon, api_key):
    """Returns a message with the weather forecast for tomorrow."""
    # API PARAMETERS
    lang = "en"
    part = "minutely,hourly"
    units = "metric"

    # API CONNECTION
    connection = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/onecall?"
            f"lat={lat}&lon={lon}&exclude={part}&lang={lang}&units={units}&appid={api_key}")
    connection.raise_for_status()
    data = connection.json()

    # Variables
    tomorrow = data["daily"][1]  # Dictionary
    tomorrows_date = datetime.date.fromtimestamp(tomorrow["dt"]).__format__("%d-%m-%Y")  # Date str
    temp = tomorrow["temp"]  # Dictionary
    feels = tomorrow["feels_like"]  # Dictionary
    weather = tomorrow["weather"][0]["description"]  # Weather description, str

    # Check for rain, snow or alerts
    try:
        rain = tomorrow['rain']
    except KeyError:
        rain = ""

    try:
        snow = tomorrow['snow']
    except KeyError:
        snow = ""

    try:  # Checks for alerts
        alerts = data['alerts']
    except KeyError:
        extra = ""
    else:
        start = datetime.date.fromtimestamp(data['alerts'][0]['start']).__format__('%d-%m-%Y')
        end = datetime.date.fromtimestamp(data['alerts'][0]['start']).__format__('%d-%m-%Y')
        if start != end:
            extra = f"!!Alert from {start} to {end}!!\n\n"
        else:
            extra = f"!!Alert: {start}!!\n\n"

    # Text building
    message = "" + extra  # Alarms
    message += f"Day: {tomorrows_date}\n"  # Date
    message += f"Sunrise: {datetime.datetime.fromtimestamp(tomorrow['sunrise']).__format__('%H:%M')}, " \
               f"sunset: {datetime.datetime.fromtimestamp(tomorrow['sunset']).__format__('%H:%M')}\n"  # Sunrise/set
    message += f"Weather: {weather.capitalize()}"  # Weather description

    if tomorrow["uvi"] > 5:
        message += " !!wear suncream!!"  # HIGH UV

    message += f"\n\nTemperature:\nMax: {temp['max']}, Min: {temp['min']} \n" \
               f"Morning: {temp['morn']}/{feels['morn']} Day: {temp['day']}/{feels['day']}\n\n"  # Temperatures
    message += f"Precipitations: {tomorrow['pop']}%\n"  # Precipitations

    if snow:
        message += f"!!Snow: {snow}mm!!\n"  # SNOW ALERT
    if rain:
        message += f"!!Rain: {rain}mm!!"  # RAIN ALERT

    return message


if __name__ == "__main__":
    print(get_tomorrows_weather(input("lat: "), input("lon: "), input("API key: ")))
