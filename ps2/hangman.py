# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # Loops every letter of letters_guessed to see if it's in the secret word
    guessed_word = list(len(secret_word)*"_")
    secret_list = list(secret_word)
    letters_copy = letters_guessed[:] # Creates a copy to the for loop
    
    for char in letters_copy:
        j = 0
        while j < len(secret_list):
            if char == secret_list[j]:
                guessed_word[j] = char
            j += 1
            
    return ' '.join(guessed_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # Gets the alphabet and turns it into a list
    import string
    available_letters = list(string.ascii_lowercase)
    
    # Loop search to remove each one of letters_guessed from the alphabet
    letters_copy = letters_guessed[:]
    for char in letters_copy:
        if char in available_letters:
            available_letters.remove(char)
    
    return ''.join(available_letters) 

def hangman(secret_word):
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # Initial constants
    guesses = 6
    warnings = 3 # Maximum: 3
    letters_guessed = []
    
    # Counts the unique letters for the score
    unique_letters = ''.join(set(secret_word))
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "long.")
    print("You have",warnings,"warnings left.")
    
    while guesses > 0:    
        print("You have",guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter = input("Please guess a letter:").lower()
        
        if letter.isalpha() == True:
        
            if letter in letters_guessed: # Checks if the letter was already guessed
                if warnings > 0:
                    warnings -= 1
                    print("Oops! You've already gussed that letter. You now have",warnings,"warnings:")
                else:
                    guesses -= 1
                    print("Oops! You've already gussed that letter.")
                    
            else: # Evaluates if the letter is in the secret word    
                letters_guessed.append(letter) # Adds the letter to the list of every letter guessed
                if letter in secret_word:
                    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                else:
                    print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    if letter in 'aeiou': # If the letter is a vowel, user losses two guesses
                        guesses -= 2
                    else: # If the letter is a consonant, uses losses one guess
                        guesses -= 1
                
        else:
            if warnings > 0:
                warnings -= 1
                print("You have",warnings,"left.")
            else:
                guesses -= 1
        
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulation, you won!")
            print("Your total score for this game is:",guesses * len(unique_letters))
            break
    else:
        print("Sorry, you ran out of guesses. The word was else.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # Removes the spaces
    word = ''
    for char in my_word:
        if char != ' ':                    # a_ple     a__le 
            word += char                    #apple     apple
    
    if len(word) != len(other_word): # Checks if the lenght is the same
        return False
    
    for i in range(len(other_word)):
        if word[i] != "_": # If the char isn't an underline, evaluates
            if word[i] != other_word[i]: # If the char is different, returns false
                return False
        else:
            if other_word[i] in word: # If the char is an underline and the char is already on word, returns false
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    matches = []
    i = 0

    # Checks every word in wordlist to see if it maches with my_word    
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            i += 1
            matches.append(other_word)
    if i == 0:
        print("No matches found")
    else: 
        print("Possible word matches are:")
        print(matches)
        print("--------")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # Initial constants
    guesses = 6
    warnings = 3 # Maximum: 3
    letters_guessed = []
    
    # Counts the unique letters for the score
    unique_letters = ''.join(set(secret_word))
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("--------")
    
    while guesses > 0:    
        print("You have",guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter = input("Please guess a letter:").lower()
        
        # Checks for hints
        if letter == "*":
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            
        else:
            
            if letter.isalpha() == True:
            
                if letter in letters_guessed: # Checks if the letter was already guessed
                    if warnings > 0:
                        warnings -= 1
                        print("Oops! You've already gussed that letter. You now have",warnings,"warnings:")
                    else:
                        guesses -= 1
                        print("Oops! You've already gussed that letter.")
                        
                else: # Evaluates if the letter is in the secret word    
                    letters_guessed.append(letter) # Adds the letter to the list of every letter guessed
                    if letter in secret_word:
                        print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                        print("------------")
                    else:
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                        print("------------")
                        if letter in 'aeiou': # If the letter is a vowel, user losses two guesses
                            guesses -= 2
                        else: # If the letter is a consonant, uses losses one guess
                            guesses -= 1
                    
            else: # Enters if the letter is not an alpha
                if warnings > 0:
                    warnings -= 1
                    print("You have",warnings,"warnings left.")
                else:
                    guesses -= 1
            
            # Checks if it's the corret word
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Congratulation, you won!")
                print("Your total score for this game is:",guesses * len(unique_letters))
                break
    else:
        print("Sorry, you ran out of guesses. The word was else.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)