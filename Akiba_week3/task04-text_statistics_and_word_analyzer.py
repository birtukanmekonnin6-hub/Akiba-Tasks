def count_words(sentence):
    words=0 
    for i in sentence:
       if i==" " or i== ".":
        words +=1
    return words
def count_characters(sentence):
    count=0
    for i in sentence:
       if i!=" " and i !=".":
          count +=1
    return count
vowels=["a","e","o","u","i"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
def count_vowels_and_consonants(sentence):
    vowel=0
    consonant=0
    for i in sentence:
       if i in vowel:
          vowel +=1
       elif i in consonants:
          consonant +=1
    return vowel, consonant

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def find_repeated_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word in word_count:
        if word_count[word] > 1:
            print(word, "appears", word_count[word], "times")




  