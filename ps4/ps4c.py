# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file.ps..")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        # pass #delete this line and replace with your code here
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        # pass #delete this line and replace with your code here
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        # pass #delete this line and replace with your code here
        
        # Initiating variables
        transpose_dict = {}
        punctuation = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        
        # Transpose the vowels
        for i, char in enumerate(vowels_permutation.lower()):
            transpose_dict[VOWELS_LOWER[i]] = char
            
        for i, char in enumerate(vowels_permutation.upper()):
            transpose_dict[VOWELS_UPPER[i]] = char
            
        # Creates a dictionary with 52 keys
        for char in CONSONANTS_LOWER:
            transpose_dict[char] = char
        for char in CONSONANTS_UPPER:
            transpose_dict[char] = char
        for punc in punctuation:
            transpose_dict[punc] = punc
        
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # pass #delete this line and replace with your code here
               
        # text = self.message_text
        # enc_message = []        
        
        # for letter in text:
        #     index = self.message_text.index(letter)
        #     enc_message.append(transpose_dict[index])        
        # return ''.join(enc_message)
        
        text = self.message_text
        enc_message = text[:]
        
        for i in range(len(text)):
            if text[i] in VOWELS_LOWER or text[i] in VOWELS_UPPER:
                enc_message = enc_message[:i] + transpose_dict[text[i]] + enc_message[i+1:]
            
        return enc_message
    
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # pass #delete this line and replace with your code here
        
        # Loop through each possible permutation
        # transpose_dict_list = [] # List of all transposed dictionaries
        # decr_list = [] # List of all decrypted messages
        perm_list = get_permutations(VOWELS_LOWER) # List of all vowel permutations
        
        # for perm in perm_list:
        #     # Checks if the decrypted message is a valid word
        #     transpose_dict_list.append(self.build_transpose_dict(perm))
        # for dic in transpose_dict_list:
        #     # Lists all decrypted possibilities
        #     decr_msg = self.apply_transpose(dic)
        #     decr_list.append(decr_msg)
            
        # # Checks if word in decrypted list is valid
        # valid_words = [] # Decrypted words to test
        # for word in decr_list:
        #     decr_words = word.split()
        #     valid_words = [i for i in decr_words if is_word(decr_words, i)]
        
        def count_valid_shifted(transpose_dict):
            # Split shifted words
            words = self.apply_transpose(transpose_dict).split()
            # Evaluates if shifted words are valid
            valid_words = [i for i in words if is_word(self.valid_words, i)]
            # Count length valid words
            return len(valid_words)
        
        # Loop shifts from each permutation
        counter = {}
        for perm in perm_list:
            counter[perm] = count_valid_shifted(perm)
        
        # Evaluates max
        optimal = max(counter, key=counter.get)
        
        # Returns tuple
        return (optimal, self.apply_transpose(optimal - 26))
            
        # If no good permutation, return original string
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
