import json

with open('key_values.json', 'r') as f:
    data = json.load(f)
# print((data.keys()))
word_number_dict = {}
list_word = []
for key in data.keys():
    for value in data[key]:
        if value not in list_word:
            list_word.append(value)
for word in list_word:
    word_number_dict[word] = []
for key in data.keys():
    for value in data[key]:
        if value in list_word:
            word_number_dict[value].append(key)

with open('word_number.json', 'w') as fp:
    json.dump(word_number_dict, fp)