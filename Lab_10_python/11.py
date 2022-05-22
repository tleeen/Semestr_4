from bs4 import BeautifulSoup
import requests

a = "http://olympus.realpython.org"
response = requests.get(a + "/profiles")
b = BeautifulSoup(response.text, "html.parser")

for link in b.find_all("a"):
    print(a + link.get("href"))