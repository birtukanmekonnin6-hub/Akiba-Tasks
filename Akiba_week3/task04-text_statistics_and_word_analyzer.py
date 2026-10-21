def count_words(sentence):
    words=0 
    for i in sentence:
       if i==" " or i== ".":
        words +=1
    return words
sentence="Python is useful and Python is powerful."
count=count_words(sentence)
print(count)