# Модуль для обработки URL
import requests
# Модуль для работы с API
import json

# Регистрируемся на сайте, получаем свой API-ключ
API_KEY = "7d3dfeb9eebc96400023e33ca4a3e622"

# Для г.Казань задаём долготу (lon) и широту (lat)
lon = 49.1221
lat = 55.7887

# Список, в котором будут храниться значения температуры за 5 дней
temperature_arr = []

# В запросе получаем погоду в Казани на 8 ближайших дней
# исключаем минутный и часовой прогнозы, предупреждения спецслужб
# используем метрическую систему
api_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric")
json_response = json.loads(api_response.text)
# Получаем из JSON утреннюю температуру для текущего и четырёх последующих дней
for i in range(5):
    temperature_arr.append(json_response["daily"][i]["temp"]["morn"])

print("Средняя утренняя температура за ближайшие пять дней ожидается", sum(temperature_arr) / 5, "\u2103"
      "\nМаксимальная утренняя температура за ближайшие пять дней ожидается", max(temperature_arr), "\u2103")