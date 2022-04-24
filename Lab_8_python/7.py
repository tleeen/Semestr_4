table = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}

with open("7_cyrillic.txt", "r", encoding="utf8") as in_file:
    a = in_file.readlines()

b = []

for i in a:
    line = ""
    for letter in i:
        if letter.lower() in table:
            if letter.isupper():
                table_letter = table[letter.lower()][0].upper(
                ) + table[letter.lower()][1:]
                line += table_letter
            else:
                line += table[letter.lower()]
        else:
            line += letter
    b.append(line)

with open("7_transliteration.txt", "w", encoding="utf8") as out_file:
    out_file.writelines(i for i in b)
