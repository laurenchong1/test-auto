'''
question2.py


Fix the errors so that this code runs when called
from the test file and passes all tests.

TOTAL POINTS AVAILABLE: 5 


Code Functionality (5)
5 points - no errors remain and code runs
4 points - only 1 error remains
1-3 points - multiple errors remain
0 points - all original errors remain or new ones introduced
'''


def decode_word(input_word):
    '''Returns the string of an emoticon for a given string. Returns an empty 
    string if input is not a known string.

    see https://en.wikipedia.org/wiki/List_of_emoticons for more about
    emoticons'''
    
    emoji_code = {'smiley':':-)', 'skeptical':':-8', 'frown':':-(', 
                  'crying':':`-(', 'surprise':':-O', 'wink':';-)', 'kiss':':-*', 
                  'tongue':':-P', 'horror':'D-:'}

    # strip word and make lower case
    input_word = input_word.strip().lower()

    # check if word is valid emoticon code
    if input_word not in emoji_code.keys():
        # return empty string
        return 
     
    # return the decoded word
    return emoji_code

def word_to_emoticon(input_string):
    '''Takes in a string containing a sequence of words and 
    returns a string where any of the words that can be represented
    by an emoticon are replaced with that emoticon.'''

    # create list of words from the string splitting at ' '
    input_list = input_string.split(',')

    # create string to be returned
    decoded_string = input_string

    # go through list of words
    for word in input_list
        # decode each word into its emoticon
        decoded_word = decode_word(word)
        # replace the word with the returned emoticon  
        if decoded_word != '':
            decoded_string = decoded_string.replace(word, decoded_word)

    # return new string of emoticons
    return decoded_string