word=input("enter the word : ")
word = word.lower()
reversed_word=""
for letter in word:
    reversed_word= letter + reversed_word
if word == reversed_word:
    print("It's palindrome")
else:
    print("It is not palindrome")