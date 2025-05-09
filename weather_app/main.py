import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import calendar
from collections import defaultdict
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="weather_app/static"), name="static")


templates = Jinja2Templates(directory="weather_app/templates")
templates.env.globals['STATIC_PREFIX'] = '/weather_app/static'

API_KEY = "22cf61ec3c1f44665e6140df5891c249"

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=cz"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=cz"

    try:
        weather_response = requests.get(weather_url, timeout=5).json()
        forecast_response = requests.get(forecast_url, timeout=5).json()

        # Ověříme, že oba požadavky byly úspěšné
        if "list" not in forecast_response or "weather" not in weather_response:
            raise ValueError("Nepodařilo se načíst data z API.")

        now = datetime.now()
        today = now.date()

        todays_data = [
            item for item in forecast_response["list"]
            if datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").date() == today
        ]

        if len(todays_data) < 8:
            needed = 8 - len(todays_data)
            future_data = [
                item for item in forecast_response["list"]
                if datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").date() > today
            ]
            todays_data += future_data[:needed]

        labels = [
            datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%H:%M")
            for item in todays_data
        ]
        temperatures = [item["main"]["temp"] for item in todays_data]
        rain_data = [item.get("rain", {}).get("3h", 0) for item in todays_data]

        forecast_by_day = defaultdict(list)
        for item in forecast_response["list"]:
            dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if dt.date() == today:
                continue
            day_name = calendar.day_name[dt.weekday()]
            forecast_by_day[day_name].append({
                "time": dt.strftime("%H:%M"),
                "temp": item["main"]["temp"],
                "description": item["weather"][0]["description"],
                "icon": item["weather"][0]["icon"],
                "humidity": item["main"]["humidity"],
                "wind": item["wind"]["speed"]
            })

        ordered_days = []
        seen = set()
        for item in forecast_response["list"]:
            dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            day = calendar.day_name[dt.weekday()]
            if dt.date() != today and day not in seen:
                ordered_days.append(day)
                seen.add(day)

        condition = weather_response["weather"][0]["main"].lower()
        backgrounds = {
            "clear": "sun.jpg",
            "clouds": "clouds.jpg",
            "rain": "rain.jpg",
            "snow": "snow.jpg",
            "thunderstorm": "storm.jpg",
            "drizzle": "rain.jpg",
            "mist": "fog.jpg"
        }
        background_image = f"{templates.env.globals['STATIC_PREFIX']}/images/{backgrounds.get(condition, 'sun.jpg')}"

        return templates.TemplateResponse("weather.html", {
            "request": request,
            "weather": weather_response,
            "labels": labels,
            "temperatures": temperatures,
            "rain_data": rain_data,
            "forecast_by_day": forecast_by_day,
            "ordered_days": ordered_days,
            "city": city,
            "background_image": background_image,
            "error": None
        })

    except Exception as e:
        print(f"❌ Chyba při zpracování požadavku: {e}")
        return templates.TemplateResponse("weather.html", {
            "request": request,
            "weather": None,
            "labels": [],
            "temperatures": [],
            "rain_data": [],
            "forecast_by_day": {},
            "ordered_days": [],
            "city": city,
            "background_image": None,
            "error": "Nepodařilo se načíst data o počasí. Zkontroluj název města nebo to zkus později."
        })


# @app.post("/weather", response_class=HTMLResponse)
# async def get_weather(request: Request, city: str = Form(...)):
#     weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=cz"
#     forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=cz"

#     weather_response = requests.get(weather_url).json()
#     forecast_response = requests.get(forecast_url).json()

#     now = datetime.now()
#     today = now.date()

#     todays_data = [
#         item for item in forecast_response["list"]
#         if datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").date() == today
#     ]

#     if len(todays_data) < 8:
#         needed = 8 - len(todays_data)
#         future_data = [
#             item for item in forecast_response["list"]
#             if datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").date() > today
#         ]
#         todays_data += future_data[:needed]

#     labels = [
#         datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%H:%M")
#         for item in todays_data
#     ]
#     temperatures = [item["main"]["temp"] for item in todays_data]
#     rain_data = [item.get("rain", {}).get("3h", 0) for item in todays_data]

#     forecast_by_day = defaultdict(list)
#     for item in forecast_response["list"]:
#         dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
#         if dt.date() == today:
#             continue
#         day_name = calendar.day_name[dt.weekday()]
#         forecast_by_day[day_name].append({
#             "time": dt.strftime("%H:%M"),
#             "temp": item["main"]["temp"],
#             "description": item["weather"][0]["description"],
#             "icon": item["weather"][0]["icon"],
#             "humidity": item["main"]["humidity"],
#             "wind": item["wind"]["speed"]
#         })

#     ordered_days = []
#     seen = set()
#     for item in forecast_response["list"]:
#         dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
#         day = calendar.day_name[dt.weekday()]
#         if dt.date() != today and day not in seen:
#             ordered_days.append(day)
#             seen.add(day)

#     condition = weather_response["weather"][0]["main"].lower()
#     backgrounds = {
#         "clear": "sun.jpg",
#         "clouds": "clouds.jpg",
#         "rain": "rain.jpg",
#         "snow": "snow.jpg",
#         "thunderstorm": "storm.jpg",
#         "drizzle": "rain.jpg",
#         "mist": "fog.jpg"
#     }
    
#     background_image = f"{templates.env.globals['STATIC_PREFIX']}/images/{backgrounds.get(condition, 'sun.jpg')}"



#     return templates.TemplateResponse("weather.html", {
#         "request": request,
#         "weather": weather_response,
#         "labels": labels,
#         "temperatures": temperatures,
#         "rain_data": rain_data,
#         "forecast_by_day": forecast_by_day,
#         "ordered_days": ordered_days,
#         "city": city,
#         "background_image": background_image
#     })

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("weather.html", {"request": request})



