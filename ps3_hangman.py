# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for value in lettersGuessed:
      # print(value)
      if value not in secretWord:
        # print('no')
        return False
    return True

# print(isWordGuessed('elvira', ['a', 'e', 'p']))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    clone = ''
    # FILL IN YOUR CODE HERE...
    for value in secretWord:
      # print(value)x`
      if value in lettersGuessed:
        # print('yes')
        clone = clone + value
        # print(clone)
      else:
        # print('no')
        clone = clone + '_ '
    return clone

# print(getGuessedWord('elvira', ['a', 'e', 'p']))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = 'abcdefghijklmnopqrstuvwxyz'
    for value in lettersGuessed:
      # print(value)
      if value in available:
        available = available.replace(value, '')
        # print(available)
    return available

# print(getAvailableLetters(['a', 'e', 'p']))



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord) ,'letters long.')

    guesses = 8
    letterGuessed = []
    guessedWord = ''


    while guesses > 0:

      print('You have ', guesses ,' guesses left.')
      avail = getAvailableLetters(letterGuessed)
      print('Available letters: ' + avail)
      guessedWord = input('Please guess a letter: ')
      guessedWord.lower()

      ##checks 
      # print('You guess is ', guessedWord)
      # print('You guesse so far', letterGuessed)
      
      
      
      if guessedWord in letterGuessed:
        show = getGuessedWord(secretWord, letterGuessed)
        print('Oops! You ve already guessed that letter: ', show ) #, + getGuessedWord(secretWord, letterGuessed))
        print('------------')
      else:
        letterGuessed.append(guessedWord) 
        if isWordGuessed(secretWord, guessedWord):
          # guessedWords = guessedWords + letterGuessed
          show = getGuessedWord(secretWord, letterGuessed)
          print('Good guess: ', show) #, + getGuessedWord(secretWord, letterGuessed) )
          print('------------')
          if show == secretWord:
            print('Congratulations, you won!')
            return
        else:
          # guessedWords = guessedWords + letterGuessed
          show = getGuessedWord(secretWord, letterGuessed)
          print('Oops! That letter is not in my word: ', show) #, + getGuessedWord(secretWord, letterGuessed) )
          print('------------')
          guesses -=1
    print('Sorry, you ran out of guesses. The word was', secretWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman('alana')

