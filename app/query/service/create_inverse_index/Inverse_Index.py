from app.query.service.create_inverse_index.Summarize_Words import summarize_words
import json
from app.query.service.constant import  URL_SORT, URL_LIST_DOCID, URL_LIST_DICT

data = summarize_words
data.sort(key=lambda item: item[0])

temp_word = data[0][0]
list_doc_id = []
list_dict = []
temp_doc=[]
temp_dict=[]
i=0

def append_dict(word, length, index):
    temp_dict.append(word)
    temp_dict.append(length)
    temp_dict.append(index)
    list_dict.append(temp_dict)

for item in data:
    if item[0] != temp_word:
        append_dict(temp_word, len(temp_doc), i)
        list_doc_id.append(temp_doc)
        temp_doc = []
        temp_dict = []
        temp_word = item[0]
        i=i+1
    temp_doc.append(item[1])
if len(temp_doc):
    list_doc_id.append(temp_doc)
    append_dict(temp_word, len(temp_doc), i )

with open(URL_SORT, 'w') as fp:
    json.dump(data, fp)

with open(URL_LIST_DOCID, 'w') as fp:
    json.dump(list_doc_id,fp)

with open(URL_LIST_DICT, 'w') as fp:
    json.dump(list_dict, fp)






