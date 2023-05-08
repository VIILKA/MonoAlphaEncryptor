import re


alphabet = 'абвгдеёжзийклмнңоөпрстуүфхцчшщъыьэюя'

list_of_analyze = [('а', 14.19460675561666), ('н', 7.498984470205918), ('к', 6.615942255413555),
                   ('ы', 6.440021248007999), ('р', 5.221385495109833), ('т', 5.114832984407712),
                   ('л', 5.037027778645752), ('е', 4.433959316314096), ('д', 4.077117770209043),
                   ('у', 4.021497984563947), ('б', 3.698090803987126), ('о', 3.5362309783457797),
                   ('и', 3.4337405868199853), ('г', 2.827547417429616), ('ү', 2.7097459613161266),
                   ('п', 2.7009967815517295), ('м', 2.6088179233196884), ('ө', 2.533200012498828),
                   ('с', 2.5135143580289347), ('й', 2.341655469799706), ('ж', 1.8520138736993406),
                   ('ш', 1.4023685279505045), ('ч', 1.3136268474830484), ('з', 1.3108146111302064),
                   ('э', 1.0405274505515107), ('ң', 0.841483610911477), ('я', 0.25778833234384274),
                   ('ю', 0.14342405399493796), ('в', 0.10592756929037903), ('х', 0.07655532293847452),
                   ('ф', 0.04843295941005531), ('ё', 0.019373183764022122), ('ц', 0.01718588882292285),
                   ('ь', 0.009374121176139736), ('i', 0.0021872949410992716)]

with open("file.txt", "r") as file:
    content = file.read()

content = content.lower()

content_copy = list(content)

result_dict = {}

for char in content:

    if char.isalpha() and char in alphabet:
        if char.lower() in result_dict:
            result_dict[char.lower()] += 1
        else:
            result_dict[char.lower()] = 1

result_dict = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))

for i in range(0, len(content)):
    if content[i] == 'я':
        content_copy[i] = 'a'

total_letters = sum(result_dict.values())
result_dict_percentage = {}
for letter, count in result_dict.items():
    percentage = count / total_letters * 100
    result_dict_percentage[letter] = percentage

print(result_dict_percentage)
finded_chars = {'я': 'а'};


def get_pattern(text: str) -> str:
    ans = ""
    alph_values = ''.join(finded_chars.values())
    alph_keys = ''.join(finded_chars.keys())
    alph_unknown = ''

    for i in range(0, len(alphabet)):
        if list(alphabet)[i] not in alph_keys:
            alph_unknown = alph_unknown + list(alphabet)[i]

    for i in range(0, len(text)):
        if list(text)[i] in alph_values:
            ans = ans + find_key(finded_chars, list(text)[i])
        else:
            ans = ans + "[" + alph_unknown + "]"
    ans = ans + ""
    return ans


def find_key(dict: dict, value) -> str:
    search_value = value
    for key, value in finded_chars.items():
        if value == search_value:
            return key


def add_new_char_in_findedList(text: str, text2: str, dictionary: dict) -> dict:
    for i in range(0, len(text2)):
        dictionary[list(text)[i]] = list(text2)[i]
    return dictionary


print(get_pattern("каныкей"))

matches = re.search(str(get_pattern("каныкей")), content)
print(add_new_char_in_findedList(str(matches.group()), "каныкей", finded_chars))

matches = re.search(str(get_pattern("манас")), content)
print(add_new_char_in_findedList(str(matches.group()), "манас", finded_chars))

matches = re.search(str(get_pattern("баатыр")), content)
print(add_new_char_in_findedList(str(matches.group()), "баатыр", finded_chars))


for i in range(0, len(content)):
    for key, value in finded_chars.items():
        if content[i] == key:
            content_copy[i] = value

unique_words = []

with open('right.txt', 'r') as file:
    for line in file:

        line = re.sub(r'[^абвгдеёжзийклмнңоөпрстуүфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНҢОӨПРСТУҮФХЦЧШЩЪЫЬЭЮЯ\s]', '', line)

        words = line.lower().split()

        for word in words:
            if word not in unique_words:
                unique_words.append(word)

print(unique_words)

for i in range (0, len(unique_words)):
    matches = re.search(str(get_pattern(unique_words[i])), content)
    if matches == None:
        continue
    else:
        add_new_char_in_findedList(str(matches.group()), unique_words[i], finded_chars)

print(finded_chars)

for i in range(0, len(content)):
    for key, value in finded_chars.items():
        if content[i] == key:
            content_copy[i] = value
print(''.join(content_copy))