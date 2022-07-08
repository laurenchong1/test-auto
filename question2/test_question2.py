'''
test_question2.py

Unit tests for question 2.
'''

import unittest
import question2 as q

class TestQuestion2(unittest.TestCase):
    def test_word(self):
        '''
        Test with single emoticon word
        '''
        result = q.word_to_emoticon('smiley')
        self.assertEqual(result, ':-)')
    
    def test_no_emoticons(self):
        '''
        Test with string with no emoticon words
        '''
        input_string = 'devoid of emotion'
        result = q.word_to_emoticon(input_string)
        self.assertEqual(result, input_string)
    
    def test_upper_emoticon(self):
        '''
        Test with emoticon word with capital letters
        '''
        result = q.word_to_emoticon('It was a Surprise party')
        self.assertEqual(result, 'It was a :-O party')

    def test_valid_sequence(self):
        '''
        Test with valid sequence
        '''
        result = q.word_to_emoticon('You better not wink and stick out your tongue at me')
        self.assertEqual(result, 'You better not ;-) and stick out your :-P at me')



if __name__ == '__main__':
    unittest.main()