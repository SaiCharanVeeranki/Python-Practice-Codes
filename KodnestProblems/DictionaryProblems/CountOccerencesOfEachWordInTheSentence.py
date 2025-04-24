Sentence = input ().lower()
words = Sentence. split()
dic_words = {}

for i in words:
    i= i.strip("., ?; ")
    if i in dic_words:
        dic_words[i] += 1
    else:
        dic_words[i] = 1
for i,j in dic_words.items ():
    print(f"{i}: {j}")