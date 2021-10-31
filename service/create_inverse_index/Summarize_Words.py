from service.create_inverse_index.Split_Words import split_words

# with open('../data/split_words.json', 'r') as f:
#     data = json.load(f)
data = split_words
word_number_dict = {}
summarize_words = []
for key in data.keys():
    for value in data[key]:
        word_num = [value, (key)]
        summarize_words.append(word_num)
# with open('../data/summarize_words.txt', 'w') as file:
#     file.write(str(summarize_words))
