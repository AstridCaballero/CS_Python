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
    f = open("week5/ps6/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'week5/ps6/words.txt'

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
        #delete this line and replace with your code here
        
        # make sure self.shift has values less than 26
        # if shift > 25:
        #     shift = self.shift % 26
        assert 0 <= shift < 26, 'shift must be a number between 0 and 25'    
        myDict = {}
       
        # add lower case keys to dictionary    
        for l in string.ascii_lowercase:
            newl = ord(l) - ord('a') + shift
            if newl > 25:
                newl -= 26 
            # add shfted value to key 
            myDict[l] = chr(newl + 97)
        # add upper case keys to dictionary
        for l in string.ascii_uppercase:
            newl = ord(l) - ord('A') + shift
            if newl > 25:
                newl -= 26
            # add shfted value to key
            myDict[l] = chr(newl + 65)        

        return myDict

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
        #delete this line and replace with your code here
        shifted_txt = ''
        temp_dict = self.build_shift_dict(shift)
        for l in self.message_text:
            if l in string.ascii_lowercase or l in string.ascii_uppercase:
                shifted_txt += temp_dict[l]
            else:
                shifted_txt += l    
        
        return shifted_txt        

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
        #delete this line and replace with your code here
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #delete this line and replace with your code here
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #delete this line and replace with your code here
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
        #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #delete this line and replace with your code here
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
        #delete this line and replace with your code here
        # store the count of valid words per new_text, if new_text 
        # is > current new_text then update new_text
        max_count = 0   
        # iterate over shift 0 to 25 and get the new_text after aplying the shift
        for i in range(0,26):
            count = 0
            new_text = Message.apply_shift(self, i)
            # clean up new_text, get rid of characters different than letters
            for l in new_text:
                if (l not in string.ascii_lowercase) and (l not in string.ascii_uppercase):
                    new_text.replace(l, ' ')
            # get a list of the cleaned up new_text. it must have only words
            new_words = new_text.split(" ")
            # check for valid words and count
            for w in new_words:                
                if is_word(Message.get_valid_words(self), w):
                    count += 1
            if count > max_count:
                max_count = count
                new_shift = i
        
        decrypted_message_text = Message.apply_shift(self, new_shift)
        return (new_shift, decrypted_message_text) 

def decrypt_story():
    myStory = CiphertextMessage(get_story_string())
    return myStory.decrypt_message()


# #Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('Abafrafr jbeqf: funer uhg pbzcbfvgvba ohfvarffyvxr ebhtu vagreehcgvba tnl snvy graq vaivgr nccyr nibvq snapl pner vzcebir urer pheerag arpx xabj she nfunzrq yrffba nalubj rkprffvir gubhtu ohfu prag svyy bja pbzzrepr ryfr qvfrnfr funec srnfg cebahapvngvba')
# print('Expected Output:', (24, 'hello!'))
# print('Actual Output:', ciphertext.decrypt_message())

# test = Message("hello")
# # shift_letter = test.build_shift_dict(2)
# # print(shift_letter)
# shift_message = test.apply_shift(1)
# print(shift_message)

# Create a CiphertextMessage object using the story string and 
# use decrypt_message to return the appropriate shift value and 
# unencrypted story string.
print(decrypt_story())
