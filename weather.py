import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data():
    print("*** Geting a weather for your city")

    city = input("Enter the city: ")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    print(requests.get(request_url).json())

get_weather_data()