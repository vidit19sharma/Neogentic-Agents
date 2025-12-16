# to access the file system
import os

# to make the http request for API call
import requests

# to import the API key from .env file
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

# look for the value with exact same name
api_key = os.getenv("OPEN_WEATHER_API_KEY")

city = "Delhi"

# formated string (f string lets you embed variable or expressions directly inside a sting)
url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city}&appid={api_key}&units=metric"
)

# making API Call
response = requests.get(url)

# convert the data into json format
data = response.json()



# printing the data
if response.status_code == 200:
    print(f"Weather in {city} : {data["weather"][0]["description"]}")
    print(f"Temprature is {data["main"]["temp"]} Celsius and feels like {data["main"]["feels_like"]} Celsius")
    # print(data)
else:
    print("Error fetching data:",data.get("message"))