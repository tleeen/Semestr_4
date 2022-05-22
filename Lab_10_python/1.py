import requests

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=86.093727%2C55.351813&spn=0.002,0.002&l=map")
print(response, type(response))
a = "1.1.png"
with open(a, "wb") as file:
    file.write(response.content)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=86.075070%2C55.321764&spn=0.002,0.002&l=map")
print(response, type(response))
a = "1.2.png"
with open(a, "wb") as file:
    file.write(response.content)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=2.294513%2C48.857747&spn=0.09,0.09&l=sat")
print(response, type(response))
a = "1.3.png"
with open(a, "wb") as file:
    file.write(response.content)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=158.848938%2C53.255097&spn=0.09,0.09&l=sat")
print(response, type(response))
a = "1.4.png"
with open(a, "wb") as file:
    file.write(response.content)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=108.655058%2C53.586278&spn=2.6,3.0&l=sat")
print(response, type(response))
a = "1.5.png"
with open(a, "wb") as file:
    file.write(response.content)
response = requests.get("https://static-maps.yandex.ru/1.x/?ll=63.309865%2C45.947975&spn=0.09,0.09&l=sat")
print(response, type(response))
a = "1.6.png"
with open(a, "wb") as file:
    file.write(response.content)
