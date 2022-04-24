import csv


with open("12_tab.csv", "r", encoding="utf-8") as product_file:
    a = csv.DictReader(product_file, delimiter=";")
    for i in a:
        name = i["Name"]
        old_price = int(i["Old price"])
        new_price = int(i["New price"])
        if old_price > new_price:
            print(name)