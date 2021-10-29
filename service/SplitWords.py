import re
import json

url= "../data/articles/nytimes"
dic = {}
for i in range(0, 1001):
    with open(url + f'{i}' + '.txt', 'r', encoding='utf-8') as f:
        str = f.read().lower()
        words = str.split()
        key_value = []
        for word in words:
            if not( word.startswith("[a-z0-9]") or word.endswith("[a-z0-9]") or word[0].isdigit() or word[-1].isdigit()):
                word = re.sub("[^a-zA-Z':-]",'', word)
                word = re.sub(r'\s+', ' ', word)
            key_value.append(word)
        key_value = list(set(key_value))
        key_value.pop(0) #remove value "" in list
    dic[i] = key_value

with open('../data/key_values.json', 'w') as fp:
  json.dump(dic, fp)