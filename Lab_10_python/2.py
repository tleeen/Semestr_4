import requests
from geocode_key import api_key

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Якутск&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Магадан&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Кемерово&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Торонто&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Хабаровск&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Уфа&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Нижний+Новгород&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Калининград&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Кемерово&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Кемерово,+ул.+Красная+6&format=json")
if response:
    print(response.content)
else:
    print("Ошибка выполнения запроса")
