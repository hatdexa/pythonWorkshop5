                     #-----Hangman Game-----

# Task1 Create string list of words for player to make guess.

import random
from this import d

words = ["apple", "orange", "banana", "coconut", "egg", "fish", "chicken", "cat", "dog", "bear", "frog", "mouse"]
lives_remaining = 14
guessed_letters = " "


def pick_a_word ():
    word_postion = random.randint(0, len(words) - 1)
    return words[word_postion]

# Task1: Test code pick a word
#print(pick_a_word())



#Task2 defind play

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You are win! Good job!")
            break
        if guess != process_guess(guess, word):
            print("You are Hung!")
            print("The word was: " + word) 
            break


#Task3 defind player lives status

def get_guess(word):
    print(str)
    print_word_with_blank(word)
    print("Lives Remaining:", + (lives_remaining))
    guess = input("Guess a letter or whole word: ")
    return guess

#Now defind print_word_with_blank to store the word in the current status every time the player makes a guess.

def print_word_with_blank(word):
    display_word = " "
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + " "
    print (display_word)



#Task4 defind the process_guess function to help the game which results to return after the player enter their guessing.

def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

#Now apply global to linked to the lives_remaining and guessed_letter of player guessing that set up as 14

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True

    else:
        lives_remaining - 1
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining

    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 0

    guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
    return True

play()







