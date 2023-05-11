import urllib.request
import random

# Import words to be guessed
# save them in list WORDS
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

# Convert bytes to string
WORDS = [x.decode("utf-8") for x in WORDS]

# Random choice of word
word = "" + random.choice(WORDS)
word_correct = word
scramble = ""

# scramble the word
while word:
    random_position = random.randint(0, len(word)-1)
    scramble += word[random_position]
    word = word[:random_position] + word[(random_position + 1):]

# game
print(
    """
            Guess the word!

            A random word is scrambled and needs your help to be unscrambled!

    """
)
print("The scrambled word is: %s" % scramble)
user_guess = input("Guess! ")
count = 1
while user_guess != word_correct:
    print("Wrong!")
    user_guess = input("Try again! ")
    if user_guess == "wtf":
        print(word_correct)
    count += 1
print("Nice, you took %s tries!" % count)