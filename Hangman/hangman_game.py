# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:57:09 2020

@author: Arijit
"""

# Hangman Game
# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in range(len(letters_guessed)):
        if letters_guessed[i] not in secret_word:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    correct_letters = ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            correct_letters = correct_letters + letter
        else:
            correct_letters = correct_letters + '_'
    
    return correct_letters



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    not_guessed = ''
     
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed = not_guessed + letter
    
    return not_guessed
    
def string_join(list_string):
    '''
    list_string: list (of letters)
    returns: a string with all the letters in the list
    '''
    out = ""
    print(out.join(list_string))

def hangman(secret_word = choose_word(wordlist)):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('The secret word is of length :' , len(secret_word))
    guessed_word = list('_') * len(secret_word)
    print('You have 6 guesses in total!')
    print('----------------------------')
    print('Available letters :' , string.ascii_lowercase)
    
    guess = 6
    while guess > 0:
        print('You have' , guess , 'guesses left!')
        letters_guessed = list(input('Enter your guess letter! ' ))
        true_letter = is_word_guessed(secret_word, letters_guessed)
        if true_letter:
            print('Excellent! You have guessed a letter correctly!')
            correct_guess = get_guessed_word(secret_word, letters_guessed)
            for i in range(len(correct_guess)):
                if correct_guess[i] in string.ascii_lowercase:
                    guessed_word[i] = correct_guess[i]
                    
        else:
            print('Oops! Guess again!')
            guess = guess - 1
        
            
            
        string_join(guessed_word)
        avail_letters = get_available_letters(letters_guessed)
        print('Available letters :' , avail_letters)
        print('----------------------------')
        
        for letter in guessed_word:
            if letter not in string.ascii_lowercase:
                break
        
        else:
            print('Congratulations! You have won!' )
            print('The correct word is : ', secret_word)
            break
        
        continue
    
    print('Sorry! You lost!\nThe correct word is : ', secret_word)
    


# -----------------------------------


if __name__ == "__main__":
    
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
