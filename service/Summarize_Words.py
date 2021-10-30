import json

with open('../data/split_words.json', 'r') as f:
    data = json.load(f)
word_number_dict = {}
list_word = []
for key in data.keys():
    for value in data[key]:
        word_num = [value, (key)]
        list_word.append(word_num)
with open('../data/summarize_words.txt', 'w') as file:
    file.write(str(list_word))