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
word = random.choice(WORDS)
hang_word = ""

# create space
for x in word:
    hang_word += "_ "

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def match_the_input(x):
    global ALPHABET
    match x:
        case "a":
            ALPHABET.remove("a")
        case "b":
            ALPHABET.remove("b")
        case "c":
            ALPHABET.remove("c")
        case "d":
            ALPHABET.remove("d")
        case "e":
            ALPHABET.remove("e")
        case "f":
            ALPHABET.remove("f")
        case "g":
            ALPHABET.remove("g")
        case "h":
            ALPHABET.remove("h")
        case "i":
            ALPHABET.remove("i")
        case "j":
            ALPHABET.remove("j")
        case "k":
            ALPHABET.remove("k")
        case "l":
            ALPHABET.remove("l")
        case "m":
            ALPHABET.remove("m")
        case "n":
            ALPHABET.remove("n")
        case "o":
            ALPHABET.remove("o")
        case "p":
            ALPHABET.remove("p")
        case "q":
            ALPHABET.remove("q")
        case "r":
            ALPHABET.remove("r")
        case "s":
            ALPHABET.remove("s")
        case "t":
            ALPHABET.remove("t")
        case "u":
            ALPHABET.remove("u")
        case "v":
            ALPHABET.remove("v")
        case "w":
            ALPHABET.remove("w")
        case "x":
            ALPHABET.remove("x")
        case "y":
            ALPHABET.remove("y")
        case "z":
            ALPHABET.remove("z")

def concat_function():
    global user_guess
    global hang_word
    user_guess = input("Your guess: ")
    while user_guess not in ALPHABET:
        print ("Invaild input! Only input from alphabet is allowed.")
        user_guess = input("Your guess: ")
    match_the_input(user_guess)
    if user_guess in word:
        index = 0
        word_temp = word
        while index != -1:
            index = word_temp.find(user_guess)
            if index < 0:
                break
            word_temp = word_temp[:index] + "1" + word_temp[index+1:]
            hang_word = hang_word[:index*2] + user_guess + hang_word[index*2 + 1:]

print("""

Hangman!
"""
      )
print("""
Try to guess the word before the man gets hanged!
    """)

print("""
    ********
    *      *
    *      *
    *
    *
    *
    *
    *
    *
    *
    *
    *
************************
    %s
""" % hang_word)
print(ALPHABET)

draw = False
fini = False
user_guess = ""

while not draw and not fini :
    concat_function()
    if "_" not in hang_word:
        fini = True
        break
    if user_guess not in word:
        draw = True
        break
    print("""
        ********
        *      *
        *      *
        *
        *
        *
        *
        *
        *
        *
        *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

if draw and not fini:
    draw = False
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *   *
        *     ***
        *
        *
        *
        *
        *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

    while not draw and not fini :
        concat_function()
        if "_" not in hang_word:
            fini = True
            break
        if user_guess not in word:
            draw = True
            break
        print("""
            ********
            *      *
            *      *
            *     ***
            *    *   *
            *     ***
            *
            *
            *
            *
            *
            *
        ************************
            %s
        """ % hang_word)
        print(ALPHABET)

if draw and not fini:
    draw = False
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *   *
        *     ***
        *      *
        *      *
        *      *
        *
        *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

    while not draw and not fini :
        concat_function()
        if "_" not in hang_word:
            fini = True
            break
        if user_guess not in word:
            draw = True
            break
        print("""
            ********
            *      *
            *      *
            *     ***
            *    *   *
            *     ***
            *      *
            *      *
            *      *
            *
            *
            *
        ************************
            %s
        """ % hang_word)
        print(ALPHABET)

if draw and not fini:
    draw = False
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *   *
        *     ***
        *      *
        *      *
        *      *
        *     *
        *    *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

    while not draw and not fini :
        concat_function()
        if "_" not in hang_word:
            fini = True
            break
        if user_guess not in word:
            draw = True
            break
        print("""
            ********
            *      *
            *      *
            *     ***
            *    *   *
            *     ***
            *      *
            *      *
            *      *
            *     *
            *    *
            *
        ************************
            %s
        """ % hang_word)
        print(ALPHABET)

if draw and not fini:
    draw = False
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *   *
        *     ***
        *      *
        *      *
        *      *
        *     * *
        *    *   *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

    while not draw and not fini :
        concat_function()
        if "_" not in hang_word:
            fini = True
            break
        if user_guess not in word:
            draw = True
            break
        print("""
            ********
            *      *
            *      *
            *     ***
            *    *   *
            *     ***
            *      *
            *      *
            *      *
            *     * *
            *    *   *
            *
        ************************
            %s
        """ % hang_word)
        print(ALPHABET)

if draw and not fini:
    draw = False
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *   *
        *     ***
        *      *
        *      * *
        *      *
        *     * *
        *    *   *
        *
    ************************
        %s
    """ % hang_word)
    print(ALPHABET)

    while not draw and not fini :
        concat_function()
        if "_" not in hang_word:
            fini = True
            break
        if user_guess not in word:
            draw = True
            break
        print("""
            ********
            *      *
            *      *
            *     ***
            *    *   *
            *     ***
            *      *
            *      * *
            *      *
            *     * *
            *    *   *
            *
        ************************
            %s
        """ % hang_word)
        print(ALPHABET)

if draw and not fini:
    print("""
        ********
        *      *
        *      *
        *     ***
        *    *x x*
        *     ***
        *      *
        *    * * *
        *      *
        *     * *
        *    *   *
        *   
    ************************
        %s
    """ % word)
    print(ALPHABET)
    print("You lose!")

if fini:
    print("""
        ********
        *      *
        *      *
        *     YOU WIN
        *       ***
        *      *   *
        *       ***
        *      * * *
        *        * 
        *        *
        *       * *
        *      *   *   
    ************************
        %s
    """ % word)
    print("You win!")
