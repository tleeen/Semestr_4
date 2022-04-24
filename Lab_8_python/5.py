import numpy as np

table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
names = table["Shrt_Desc"]
Energ_Kcal = table["Energ_Kcal"]
Sugar_Tot = table["Sugar_Tot"]
Protein = table["Protein"]
Vit_C = table["Vit_C"]

i_Energ_Kcal = np.argmax(Energ_Kcal[::-1])
i_Sugar_Tot = np.argmin(Sugar_Tot)
i_Protein = np.argmax(Protein)
i_Vit_C = np.argmax(Vit_C)

print("Cамый калорийный: " + names[len(table) - i_Energ_Kcal])
print("Самый полезный по содержанию сахара: " + names[i_Sugar_Tot])
print("Самый протеино-накачанный: " + names[i_Protein])
print("Самый богатый витамином С: " + names[i_Vit_C])
