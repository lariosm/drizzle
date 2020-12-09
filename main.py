# Baltazar Ortiz
import os
from datetime import datetime
import requests
import json

def is_raining(value):
    return value >= 500 and value < 600

url = "https://api.openweathermap.org/data/2.5/onecall"
url = url + "?lat=44.950433005684886&lon=-122.99038677842634"
url = url + "&exclude=current,minutely&appid="
url = url + os.getenv('API_KEY')
url = url + "&units=imperial"

# r = requests.get(url)
# data = r.json()
# print(data)

x = """{
    "lat": 44.95,
    "lon": -122.99,
    "timezone": "America/Los_Angeles",
    "timezone_offset": -28800,
    "hourly": [
        {
            "dt": 1607461200,
            "temp": 52.48,
            "feels_like": 50.25,
            "pressure": 1022,
            "humidity": 76,
            "dew_point": 45.16,
            "uvi": 0.91,
            "clouds": 1,
            "visibility": 10000,
            "wind_speed": 1.95,
            "wind_deg": 223,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607464800,
            "temp": 53.04,
            "feels_like": 50.56,
            "pressure": 1021,
            "humidity": 70,
            "dew_point": 43.54,
            "uvi": 0.69,
            "clouds": 47,
            "visibility": 10000,
            "wind_speed": 1.77,
            "wind_deg": 243,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607468400,
            "temp": 52.77,
            "feels_like": 51.06,
            "pressure": 1019,
            "humidity": 73,
            "dew_point": 44.37,
            "uvi": 0.34,
            "clouds": 75,
            "visibility": 10000,
            "wind_speed": 0.72,
            "wind_deg": 240,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607472000,
            "temp": 49.48,
            "feels_like": 46.94,
            "pressure": 1019,
            "humidity": 77,
            "dew_point": 42.58,
            "uvi": 0,
            "clouds": 91,
            "visibility": 10000,
            "wind_speed": 1.5,
            "wind_deg": 166,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607475600,
            "temp": 47.64,
            "feels_like": 43.09,
            "pressure": 1019,
            "humidity": 78,
            "dew_point": 41.13,
            "uvi": 0,
            "clouds": 74,
            "visibility": 10000,
            "wind_speed": 4.54,
            "wind_deg": 152,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.03
        },
        {
            "dt": 1607479200,
            "temp": 47.25,
            "feels_like": 42.37,
            "pressure": 1019,
            "humidity": 79,
            "dew_point": 41.29,
            "uvi": 0,
            "clouds": 88,
            "visibility": 10000,
            "wind_speed": 5.1,
            "wind_deg": 172,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.06
        },
        {
            "dt": 1607482800,
            "temp": 48.24,
            "feels_like": 43.29,
            "pressure": 1019,
            "humidity": 78,
            "dew_point": 41.86,
            "uvi": 0,
            "clouds": 88,
            "visibility": 10000,
            "wind_speed": 5.46,
            "wind_deg": 186,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.1
        },
        {
            "dt": 1607486400,
            "temp": 48.27,
            "feels_like": 43.45,
            "pressure": 1019,
            "humidity": 79,
            "dew_point": 42.22,
            "uvi": 0,
            "clouds": 87,
            "visibility": 10000,
            "wind_speed": 5.37,
            "wind_deg": 200,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.29
        },
        {
            "dt": 1607490000,
            "temp": 48.31,
            "feels_like": 44.15,
            "pressure": 1019,
            "humidity": 87,
            "dew_point": 44.76,
            "uvi": 0,
            "clouds": 90,
            "visibility": 6670,
            "wind_speed": 5.14,
            "wind_deg": 227,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n"
                }
            ],
            "pop": 0.59,
            "rain": {
                "1h": 1.3
            }
        },
        {
            "dt": 1607493600,
            "temp": 48.81,
            "feels_like": 45.16,
            "pressure": 1020,
            "humidity": 94,
            "dew_point": 47.3,
            "uvi": 0,
            "clouds": 91,
            "visibility": 10000,
            "wind_speed": 5.35,
            "wind_deg": 204,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n"
                }
            ],
            "pop": 0.8,
            "rain": {
                "1h": 1.26
            }
        },
        {
            "dt": 1607497200,
            "temp": 50.32,
            "feels_like": 47.05,
            "pressure": 1021,
            "humidity": 93,
            "dew_point": 48.6,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 5.21,
            "wind_deg": 252,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "pop": 0.99,
            "rain": {
                "1h": 0.31
            }
        },
        {
            "dt": 1607500800,
            "temp": 49.78,
            "feels_like": 47.19,
            "pressure": 1021,
            "humidity": 94,
            "dew_point": 48.34,
            "uvi": 0,
            "clouds": 100,
            "visibility": 8058,
            "wind_speed": 3.87,
            "wind_deg": 233,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n"
                }
            ],
            "pop": 1,
            "rain": {
                "1h": 1.15
            }
        },
        {
            "dt": 1607504400,
            "temp": 49.62,
            "feels_like": 46.26,
            "pressure": 1022,
            "humidity": 93,
            "dew_point": 47.8,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 5.03,
            "wind_deg": 248,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "pop": 1,
            "rain": {
                "1h": 0.94
            }
        },
        {
            "dt": 1607508000,
            "temp": 49.39,
            "feels_like": 44.64,
            "pressure": 1023,
            "humidity": 90,
            "dew_point": 46.62,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 7.02,
            "wind_deg": 264,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.8
        },
        {
            "dt": 1607511600,
            "temp": 46.9,
            "feels_like": 42.04,
            "pressure": 1024,
            "humidity": 90,
            "dew_point": 44.19,
            "uvi": 0,
            "clouds": 89,
            "visibility": 10000,
            "wind_speed": 6.22,
            "wind_deg": 277,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.8
        },
        {
            "dt": 1607515200,
            "temp": 44.91,
            "feels_like": 40.75,
            "pressure": 1025,
            "humidity": 91,
            "dew_point": 42.51,
            "uvi": 0,
            "clouds": 76,
            "visibility": 10000,
            "wind_speed": 4.32,
            "wind_deg": 273,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.8
        },
        {
            "dt": 1607518800,
            "temp": 43.45,
            "feels_like": 40.24,
            "pressure": 1025,
            "humidity": 92,
            "dew_point": 41.43,
            "uvi": 0,
            "clouds": 19,
            "visibility": 10000,
            "wind_speed": 2.19,
            "wind_deg": 268,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ],
            "pop": 0.14
        },
        {
            "dt": 1607522400,
            "temp": 42.78,
            "feels_like": 40.01,
            "pressure": 1025,
            "humidity": 93,
            "dew_point": 40.95,
            "uvi": 0,
            "clouds": 50,
            "visibility": 10000,
            "wind_speed": 1.3,
            "wind_deg": 231,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "pop": 0.06
        },
        {
            "dt": 1607526000,
            "temp": 42.22,
            "feels_like": 39.31,
            "pressure": 1026,
            "humidity": 93,
            "dew_point": 40.48,
            "uvi": 0,
            "clouds": 52,
            "visibility": 10000,
            "wind_speed": 1.36,
            "wind_deg": 190,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0.05
        },
        {
            "dt": 1607529600,
            "temp": 42.04,
            "feels_like": 38.91,
            "pressure": 1027,
            "humidity": 93,
            "dew_point": 40.37,
            "uvi": 0,
            "clouds": 62,
            "visibility": 10000,
            "wind_speed": 1.68,
            "wind_deg": 191,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0.01
        },
        {
            "dt": 1607533200,
            "temp": 44.69,
            "feels_like": 41.68,
            "pressure": 1027,
            "humidity": 91,
            "dew_point": 42.42,
            "uvi": 0.22,
            "clouds": 53,
            "visibility": 10000,
            "wind_speed": 2.19,
            "wind_deg": 191,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607536800,
            "temp": 47.61,
            "feels_like": 44.56,
            "pressure": 1028,
            "humidity": 86,
            "dew_point": 43.75,
            "uvi": 0.53,
            "clouds": 44,
            "visibility": 10000,
            "wind_speed": 2.77,
            "wind_deg": 206,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607540400,
            "temp": 49.96,
            "feels_like": 47.41,
            "pressure": 1028,
            "humidity": 81,
            "dew_point": 44.46,
            "uvi": 0.82,
            "clouds": 3,
            "visibility": 10000,
            "wind_speed": 2.21,
            "wind_deg": 209,
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607544000,
            "temp": 51.12,
            "feels_like": 48.24,
            "pressure": 1027,
            "humidity": 78,
            "dew_point": 44.65,
            "uvi": 1,
            "clouds": 33,
            "visibility": 10000,
            "wind_speed": 2.84,
            "wind_deg": 229,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607547600,
            "temp": 51.64,
            "feels_like": 48.96,
            "pressure": 1027,
            "humidity": 76,
            "dew_point": 44.56,
            "uvi": 0.92,
            "clouds": 55,
            "visibility": 10000,
            "wind_speed": 2.42,
            "wind_deg": 242,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607551200,
            "temp": 51.8,
            "feels_like": 49.05,
            "pressure": 1026,
            "humidity": 75,
            "dew_point": 44.38,
            "uvi": 0.63,
            "clouds": 51,
            "visibility": 10000,
            "wind_speed": 2.46,
            "wind_deg": 293,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607554800,
            "temp": 51.08,
            "feels_like": 49.03,
            "pressure": 1026,
            "humidity": 79,
            "dew_point": 44.96,
            "uvi": 0.32,
            "clouds": 61,
            "visibility": 10000,
            "wind_speed": 1.48,
            "wind_deg": 334,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607558400,
            "temp": 47.37,
            "feels_like": 44.98,
            "pressure": 1026,
            "humidity": 86,
            "dew_point": 43.61,
            "uvi": 0,
            "clouds": 68,
            "visibility": 10000,
            "wind_speed": 1.54,
            "wind_deg": 4,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607562000,
            "temp": 44.62,
            "feels_like": 41.72,
            "pressure": 1027,
            "humidity": 89,
            "dew_point": 41.77,
            "uvi": 0,
            "clouds": 71,
            "visibility": 10000,
            "wind_speed": 1.74,
            "wind_deg": 19,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607565600,
            "temp": 43.5,
            "feels_like": 40.35,
            "pressure": 1026,
            "humidity": 90,
            "dew_point": 41.04,
            "uvi": 0,
            "clouds": 41,
            "visibility": 10000,
            "wind_speed": 1.9,
            "wind_deg": 45,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607569200,
            "temp": 42.6,
            "feels_like": 39.33,
            "pressure": 1026,
            "humidity": 91,
            "dew_point": 40.37,
            "uvi": 0,
            "clouds": 37,
            "visibility": 10000,
            "wind_speed": 1.92,
            "wind_deg": 69,
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607572800,
            "temp": 41.92,
            "feels_like": 38.79,
            "pressure": 1026,
            "humidity": 92,
            "dew_point": 39.85,
            "uvi": 0,
            "clouds": 52,
            "visibility": 10000,
            "wind_speed": 1.52,
            "wind_deg": 46,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607576400,
            "temp": 41.58,
            "feels_like": 37.83,
            "pressure": 1025,
            "humidity": 92,
            "dew_point": 39.61,
            "uvi": 0,
            "clouds": 62,
            "visibility": 10000,
            "wind_speed": 2.51,
            "wind_deg": 30,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607580000,
            "temp": 40.73,
            "feels_like": 36.63,
            "pressure": 1025,
            "humidity": 93,
            "dew_point": 39,
            "uvi": 0,
            "clouds": 68,
            "visibility": 10000,
            "wind_speed": 2.95,
            "wind_deg": 4,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607583600,
            "temp": 39.99,
            "feels_like": 35.44,
            "pressure": 1024,
            "humidity": 94,
            "dew_point": 38.5,
            "uvi": 0,
            "clouds": 99,
            "visibility": 10000,
            "wind_speed": 3.6,
            "wind_deg": 359,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607587200,
            "temp": 39.18,
            "feels_like": 34.72,
            "pressure": 1023,
            "humidity": 94,
            "dew_point": 37.87,
            "uvi": 0,
            "clouds": 99,
            "visibility": 10000,
            "wind_speed": 3.2,
            "wind_deg": 355,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607590800,
            "temp": 38.39,
            "feels_like": 33.78,
            "pressure": 1023,
            "humidity": 95,
            "dew_point": 37.15,
            "uvi": 0,
            "clouds": 91,
            "visibility": 10000,
            "wind_speed": 3.29,
            "wind_deg": 38,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607594400,
            "temp": 37.92,
            "feels_like": 33.12,
            "pressure": 1022,
            "humidity": 94,
            "dew_point": 36.61,
            "uvi": 0,
            "clouds": 94,
            "visibility": 10000,
            "wind_speed": 3.42,
            "wind_deg": 28,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607598000,
            "temp": 37.4,
            "feels_like": 32.68,
            "pressure": 1021,
            "humidity": 94,
            "dew_point": 35.94,
            "uvi": 0,
            "clouds": 94,
            "visibility": 10000,
            "wind_speed": 3.11,
            "wind_deg": 19,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607601600,
            "temp": 36.82,
            "feels_like": 32.2,
            "pressure": 1020,
            "humidity": 94,
            "dew_point": 35.42,
            "uvi": 0,
            "clouds": 95,
            "visibility": 10000,
            "wind_speed": 2.77,
            "wind_deg": 12,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607605200,
            "temp": 36.39,
            "feels_like": 32.18,
            "pressure": 1019,
            "humidity": 94,
            "dew_point": 34.92,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 1.9,
            "wind_deg": 346,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607608800,
            "temp": 36.55,
            "feels_like": 32.45,
            "pressure": 1019,
            "humidity": 96,
            "dew_point": 35.56,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 1.9,
            "wind_deg": 333,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607612400,
            "temp": 36.97,
            "feels_like": 32.94,
            "pressure": 1018,
            "humidity": 95,
            "dew_point": 35.8,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 1.83,
            "wind_deg": 77,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607616000,
            "temp": 36.64,
            "feels_like": 33.35,
            "pressure": 1018,
            "humidity": 95,
            "dew_point": 35.42,
            "uvi": 0,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 0.43,
            "wind_deg": 207,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607619600,
            "temp": 38.64,
            "feels_like": 34.92,
            "pressure": 1017,
            "humidity": 92,
            "dew_point": 36.68,
            "uvi": 0.21,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 1.54,
            "wind_deg": 200,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607623200,
            "temp": 40.77,
            "feels_like": 36.16,
            "pressure": 1017,
            "humidity": 88,
            "dew_point": 37.53,
            "uvi": 0.5,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 3.42,
            "wind_deg": 178,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607626800,
            "temp": 42.37,
            "feels_like": 36.57,
            "pressure": 1017,
            "humidity": 84,
            "dew_point": 38.14,
            "uvi": 0.68,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 5.64,
            "wind_deg": 179,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        },
        {
            "dt": 1607630400,
            "temp": 42.85,
            "feels_like": 36.14,
            "pressure": 1017,
            "humidity": 85,
            "dew_point": 38.84,
            "uvi": 0.83,
            "clouds": 100,
            "visibility": 10000,
            "wind_speed": 7.52,
            "wind_deg": 192,
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "pop": 0
        }
    ],
    "daily": [
        {
            "dt": 1607457600,
            "sunrise": 1607441878,
            "sunset": 1607473840,
            "temp": {
                "day": 52.27,
                "min": 40.82,
                "max": 53.04,
                "night": 50.32,
                "eve": 47.25,
                "morn": 40.82
            },
            "feels_like": {
                "day": 49.14,
                "night": 47.05,
                "eve": 42.37,
                "morn": 36.93
            },
            "pressure": 1021,
            "humidity": 63,
            "dew_point": 40.14,
            "wind_speed": 1.63,
            "wind_deg": 233,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 97,
            "pop": 0.99,
            "rain": 2.87,
            "uvi": 0.99
        },
        {
            "dt": 1607544000,
            "sunrise": 1607528333,
            "sunset": 1607560237,
            "temp": {
                "day": 51.12,
                "min": 39.99,
                "max": 51.8,
                "night": 39.99,
                "eve": 43.5,
                "morn": 42.78
            },
            "feels_like": {
                "day": 48.24,
                "night": 35.44,
                "eve": 40.35,
                "morn": 40.01
            },
            "pressure": 1027,
            "humidity": 78,
            "dew_point": 44.65,
            "wind_speed": 2.84,
            "wind_deg": 229,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 33,
            "pop": 1,
            "rain": 2.09,
            "uvi": 1
        },
        {
            "dt": 1607630400,
            "sunrise": 1607614787,
            "sunset": 1607646637,
            "temp": {
                "day": 42.85,
                "min": 36.39,
                "max": 43.43,
                "night": 40.44,
                "eve": 41.29,
                "morn": 36.55
            },
            "feels_like": {
                "day": 36.14,
                "night": 33.01,
                "eve": 35.17,
                "morn": 32.45
            },
            "pressure": 1017,
            "humidity": 85,
            "dew_point": 38.84,
            "wind_speed": 7.52,
            "wind_deg": 192,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 0.66,
            "rain": 0.56,
            "uvi": 0.83
        },
        {
            "dt": 1607716800,
            "sunrise": 1607701239,
            "sunset": 1607733039,
            "temp": {
                "day": 42.66,
                "min": 36.97,
                "max": 42.87,
                "night": 39.74,
                "eve": 40.71,
                "morn": 37.92
            },
            "feels_like": {
                "day": 36.34,
                "night": 35.08,
                "eve": 35.58,
                "morn": 30.33
            },
            "pressure": 1021,
            "humidity": 88,
            "dew_point": 39.43,
            "wind_speed": 7.05,
            "wind_deg": 179,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 8.5,
            "uvi": 0.5
        },
        {
            "dt": 1607803200,
            "sunrise": 1607787688,
            "sunset": 1607819444,
            "temp": {
                "day": 42.96,
                "min": 39.74,
                "max": 49.68,
                "night": 45.68,
                "eve": 49.68,
                "morn": 41.36
            },
            "feels_like": {
                "day": 38.8,
                "night": 40.78,
                "eve": 44.78,
                "morn": 37.04
            },
            "pressure": 1011,
            "humidity": 97,
            "dew_point": 42.44,
            "wind_speed": 4.23,
            "wind_deg": 32,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 34.13,
            "uvi": 0.62
        },
        {
            "dt": 1607889600,
            "sunrise": 1607874136,
            "sunset": 1607905852,
            "temp": {
                "day": 47.5,
                "min": 43.57,
                "max": 48.09,
                "night": 44.26,
                "eve": 45.18,
                "morn": 44.11
            },
            "feels_like": {
                "day": 41.85,
                "night": 37.96,
                "eve": 35.56,
                "morn": 38.59
            },
            "pressure": 1014,
            "humidity": 89,
            "dew_point": 44.58,
            "wind_speed": 7.74,
            "wind_deg": 142,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 14,
            "uvi": 1
        },
        {
            "dt": 1607976000,
            "sunrise": 1607960581,
            "sunset": 1607992262,
            "temp": {
                "day": 49.12,
                "min": 41.32,
                "max": 49.12,
                "night": 46.65,
                "eve": 46.62,
                "morn": 41.32
            },
            "feels_like": {
                "day": 41.45,
                "night": 34.93,
                "eve": 37.27,
                "morn": 34.32
            },
            "pressure": 1024,
            "humidity": 80,
            "dew_point": 43.47,
            "wind_speed": 10.85,
            "wind_deg": 196,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 54,
            "pop": 1,
            "rain": 13.07,
            "uvi": 1
        },
        {
            "dt": 1608062400,
            "sunrise": 1608047025,
            "sunset": 1608078675,
            "temp": {
                "day": 49.95,
                "min": 42.4,
                "max": 49.95,
                "night": 43.63,
                "eve": 44.08,
                "morn": 42.4
            },
            "feels_like": {
                "day": 43.25,
                "night": 39.83,
                "eve": 40.75,
                "morn": 34.41
            },
            "pressure": 1016,
            "humidity": 70,
            "dew_point": 40.59,
            "wind_speed": 8.14,
            "wind_deg": 251,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "clouds": 65,
            "pop": 0.96,
            "rain": 5.72,
            "uvi": 1
        }
    ]
}"""

y = json.loads(x)
next_day = y["daily"][1]
weather_tomorrow = next_day["weather"][0]
startRainTime = 0
if is_raining(weather_tomorrow["id"]):
    for i in range(int(len(y["hourly"]) / 2)):
        current_hour_weather = y["hourly"][i]["weather"][0]["id"]
        if is_raining(current_hour_weather):
            startRainTime = datetime.fromtimestamp(y["hourly"][i]["dt"])
            break
    print(f"It will start raining at: {startRainTime}")
else:
    print("it will not rain")
