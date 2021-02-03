import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
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

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open('D:\\Dev\\Intro to CS\\Week5 OOO\\Problem6\\story.text', "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'
STORY_FILENAME = 'd:/Dev/Intro to CS/Week5 OOO/Problem6/story.text'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if (shift <26 and shift>=0):
                
            import string
            letrasLow = string.ascii_lowercase
            letrasUp = string.ascii_uppercase
            alphabet = letrasLow + letrasUp
            # print(letras)
            lFirst = letrasLow[0:shift]
            lSecond = letrasLow[shift:]
            letrasShifted = lSecond+lFirst


            lUpFirst = letrasUp[0:shift]
            lUpSecond = letrasUp[shift:]
            letrasShiftedUp = lUpSecond+lUpFirst

            letras = letrasShifted+ letrasShiftedUp


            # print(letrasShifted)
            myDict = {}
            for i in range(len(alphabet)):
                valLetras = alphabet[i]
                if valLetras not in myDict:
                    myDict[valLetras] = letras[i]    
                else:
                    continue
            
            return myDict
        else:
            return print('Invalid shift number! Enter a number between 0 and 25')


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dicionario = self.build_shift_dict(shift)
        # print(dicionario)
        returnMsg = ''
        for value in self.message_text:
            if value in dicionario:
                returnMsg = returnMsg + dicionario[value]
            else:
                returnMsg = returnMsg + value
        return returnMsg

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.change_shift(shift)

        
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if (shift <26 and shift >=0):
            self.shift = shift
            self.encrypting_dict = self.build_shift_dict(self.shift)
            self.message_text_encrypted = self.apply_shift(self.shift)
        else:
            return

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        #so we need get a message and break that into different words using slice
        #we will discard spaces and punctuations
        # we will make this list so we can compare that with the words
        ## use re to split and get rid of spaces, punctuations and etc
        import re
        #load the wordlist - we will use this to find out the best result after trying all shifts
        wordList = self.get_valid_words()

        #try different shifts and compare the number of answers.
        #initialize the attributes
        myShift = 25
        bestOption = {} #dictionary to save all the results
        maxSuCounter = [] # list to save all results from counter


        while myShift >=0:

            shiftMessage = self.apply_shift(myShift)
            sText = re.split(r'[;!,\s]\s*', shiftMessage)
            # print(sText) # check if the message is spliting correctly after the shift
            counter = 0
            maxCounter = len(sText) # calculate the phrase length, we will use this so if the number of words match this number we found the best solution which is 100% deciphered
            # print(maxCounter) # check the total

            ##loop through each shifted word and check if that is in ourlist; increment our counter for each positive result
            for word in sText:
                if word in wordList:
                    counter+=1
            maxSuCounter.append(counter)

            ###Alternative ways of saving (this was just a test)
            # bestOption.update({ counter: [myShift, shiftMessage]}) #This works with solution 1
            # bestOption.update({ myShift: [counter, myShift, shiftMessage]}) #Trying with Solution 2

            #save the results inside a dictionary
            bestOption[myShift] = {'shift': myShift, 'counter': counter, 'message': shiftMessage}

            #if our counter matches our maxCounter; then we found the best result; return it and end the computation
            if counter == maxCounter:
                return ((myShift), sText)
            #decrease our shift to try a different one
            myShift-=1

        # print(bestOption) # check results
        # print(maxSuCounter) # check if this is not empty

        #loop through the results in dictionary and save all the maxSuCounter inside a list (OLD CODE since this was optimized)
        # maxSuCounter = []
        # for values in bestOption.values():
        #     maxSuCounter.append(values['counter'])
        # print(maxSuCounter) # check
        # print(max(maxSuCounter)) # check 

        for values in bestOption.values():
            if values['counter'] == max(maxSuCounter):
                return values['shift'], values['message']


        ##Loop through dictionary and get the best result (TRYING Solution 2)
        # for values in bestOption.values():
        #     print(values[1])
        #     # print(key[0]) #acessing the value 1
        #     print(max(bestOption.values()))
        #     if (values[0] == max(bestOption.values())):
        #         return values[1], values[2]
        #     # if key == max(bestOption.keys()):
        #     #     return bestOption[key][0], bestOption[key][1]

        ##Loop through dictionary and get the best result (Working) SOLUTUON 1
        # for key in bestOption.keys():
        #     print(key)
        #     if key == max(bestOption.keys()):
        #         return bestOption[key][0], bestOption[key][1]

# My Test
# test = Message('Hello my, man!.')
# print('Alphabet:', test.build_shift_dict(25))
# # print('Inverted Word:', test.apply_shift(2))

# Example test case (PlaintextMessage)


class CipherStory(CiphertextMessage):
    def __init__(self, text):
        Message.__init__(self, text)


    def decrypt_message(self):
        return self.decrypt_message

# plaintext = PlaintextMessage('I would say hello where are you going pretty', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())

    
#Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq')
# ciphertext = CiphertextMessage('K yqwnf uca jgnnq yjgtg ctg aqw iqkpi rtgvva')

# # ciphertext = CiphertextMessage('I love you beautiful women and I want to have a family with you')
# # print('Expected Output:', (24, 'hello'))
# print('Expected Output:', (24, 'I would say hello where are you going pretty'))
# print('Actual Output:', ciphertext.decrypt_message())


##MY CIPHER
cipherStory = get_story_string()
print(cipherStory)
# print('Output', cipherStory.decrypt_message())

#####Code to get the path
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# def build_shift_dict(self, shift):
#     '''
#     Creates a dictionary that can be used to apply a cipher to a letter.
#     The dictionary maps every uppercase and lowercase letter to a
#     character shifted down the alphabet by the input shift. The dictionary
#     should have 52 keys of all the uppercase letters and all the lowercase
#     letters only.        
    
#     shift (integer): the amount by which to shift every letter of the 
#     alphabet. 0 <= shift < 26

#     Returns: a dictionary mapping a letter (string) to 
#                 another letter (string). 
#     '''
#     pass #delete this line and replace with your code here
#     import string
#     # print(string.ascii_lowercase)
#     # print(string.ascii_uppercase)

#     letras = string.ascii_lowercase + string.ascii_uppercase
#     test = ''
#     # print(letras)
#     lFirst = letras[0:shift]
#     lSecond = letras[shift :]
#     print(lSecond + lFirst)

#     # for i in range(len(letras)):
#     #     test = letras[(i)]

#     # print(test)

#     myDict = {}
#     for i in letras:
#         if i not in myDict:
#             myDict[i] = i      
#         else:
#             continue
    
#     print(myDict)
#     print(len(myDict))

# print(build_shift_dict('self', 3))
