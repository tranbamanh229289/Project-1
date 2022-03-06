import re
import json
from app.query.service.constant import URL_BASE_ARTICLE, URL_SPLIT_WORDS, N_ARTICLE

split_words = {}
for i in range(0, N_ARTICLE):
    with open(URL_BASE_ARTICLE + f'{i}' + '.txt', 'r', encoding='utf-8') as f:
        str = f.read().lower()
        words = str.split()
        key_value = []
        for word in words:
            if (not word.startswith("[a-z0-9]")) or (not word.endswith("[a-z0-9]")) \
                or (not word[0].isdigit()) or (not word[-1].isdigit()):
                word = re.sub("[^a-z0-9':-]",'', word)
                word = re.sub(r'\s+', ' ', word)
            if (word != "") and (word not in key_value) :
                key_value.append(word)
        # key_value = list(set(key_value))
        # key_value.pop(0) #remove value "" in list
    split_words[i] = key_value

with open(URL_SPLIT_WORDS, 'w') as fp:
  json.dump(split_words, fp)
