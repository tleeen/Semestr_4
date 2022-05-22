from bs4 import BeautifulSoup
import requests
from random import choice

a = "https://quotes.toscrape.com/"
p = "page/"
count_p = 10
ci = []

for i in range(count_p):
    response = requests.get(a + p + str(i + 1))
    b = BeautifulSoup(response.text, "html.parser")
    for quote in b.find_all("span", class_="text"):
        ci.append(quote.text)

for i in range(5):
    print(i + 1, ")", sep="")
    print(choice(ci))
