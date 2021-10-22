import re
import json

url= ".\data\Articles\\nytimes"
dic = {}
i = 1
for i in range(1,1001):
  with open(url + f'{i}' + '.txt', 'r', encoding='utf-8') as f:
      str = f.read().lower()
      words = []
    # Xoa dau cau va so
      sentence = re.sub("[^a-zA-Z’]", ' ', str)
    #   # Xoa ki tu don
      # sentence = re.sub(r"\s+[a-zA-Z']\s+", ' ', sentence)
    #   # Xoa nhieu space
      sentence = re.sub(r'\s+', ' ', sentence)
      for word in sentence.split():  
        if word not in  words:
            words.append(word)   
  dic[i] = words

with open('key_values.json', 'w') as fp:
  json.dump(dic, fp)
