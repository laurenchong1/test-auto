'''
question7_solution.py

Corresponding solution file for question7.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.



TOTAL POINTS AVAILABLE: 30 


Code Functionality (5 points per method, 20 across whole class)
5 points - all tests pass and code is efficient and Pythonic

4 points - all tests pass, but code could be significantly 
improved to be more Pythonic

2-3 points - at least one test fails, but much of code does work and 
rest would work with small changes

1 point - no test passes and effort has been made to answer question 
but would need significant changes/additions to make any of the code 
function correctly

0 points - no effort made to answer question



Code Readability (10 across whole file)
10 points - Well commented, clear code where PyLint returns no or 
few errors (error related to removing else/elif can be ignored)

6-9 points - Most of the code is using good practice with comments, docstrings
and names, but there is room for improvement

1-5 points - Many issues related to problems such as dense, unexplained lines
of code and variable names could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand

'''

# Create a class called MealDeal with the following class attribute:
#    meal_options = {'hot':['soup', 'panini'], 
#                    'cold':['sandwich', 'salad']}

class MealDeal():
    '''MealDeal class.'''
    # list of possible meal types
    meal_options = {'hot':['soup', 'panini'], 
                    'cold':['sandwich', 'salad']}

# Create a constructor which takes two input arguments 'meal_type' and
# 'items'. 
# 
# Check that the value of 'meal_type' is one of the keys in the
# class attribute meal_options. If not, raise a ValueError. If it is valid, 
# create an instance attribute called meal_type and set it to the passed 
# in value.
# 
# Also create an instance attribute called items which is the list of items
# passed as an input argument.
    def __init__(self, meal_type, items):
        '''Initialise a meal and whether it is hot or cold. Raise a 
        ValueError if not a valid option.'''
        # check if input is valid option
        if meal_type in MealDeal.meal_options.keys(): 
            # create and update instance attribute
            self.meal_type = meal_type
        # if not valid type
        else:
            # raise a ValueError
            raise ValueError
        # list of items
        self.items = items


# Create a method called is_valid_meal() which returns True or False according
# to whether the items in the meal create a valid meal deal.
# 
# A meal is valid if it:
#      - contains a multiple of 4 items (4, 8, 12, etc)
#      - contains one hot or cold item as defined in the class attribute for 
#        every 4 items (eg. a hot meal of 8 items can have one soup and 
#        one panini)
# 
# Ensure that you have not changed the original list of items when doing these checks.
    def is_valid_meal(self):
        '''Returns if is a valid meal deal.'''
        # check if non-empty list and if a multiple of 4 items in the meal deal
        if len(self.items)%4 == 0 and len(self.items) > 0:
            # check how many multiples of 4
            num_key_items = len(self.items)/4
            # create counter of key items encountered
            counter = 0
            # go through list and count the key items
            for i in self.items:
                if i in MealDeal.meal_options[self.meal_type]:
                    counter += 1
            # check if counted items is desired amount
            if counter == num_key_items:
                return True
        
        # not a multiple of 4
        return False
        
    
# Override the string method so that when printing a meal instance, the text nicely 
# outputs the contents of the meal. 
# Use the format:
#     The meal contains X [hot or cold] items: [item1] [item2] 
#     The remaining items are: [item3] [item4] [item5] [item6]
#  
# Such as:
#    The meal contains 2 hot items: sandwich, panini 
#    The remaining items are crisps, water, apple
    def __str__(self):
        '''Return meal contents'''
        # count number of key items 
        counter = 0
        # go through list and count the key items 
        # add to one of two lists according to if key or not
        key_items = []
        non_key_items = []
        for i in self.items:
            if i in MealDeal.meal_options[self.meal_type]:
                counter += 1
                key_items.append(i)
            else:
                non_key_items.append(i)
        # first part of string
        sentence = f'The meal contains {counter} {self.meal_type} items: '
        # string of key items
        for i in key_items:
            sentence += i +' ' 
        # first part of second sentence
        sentence += '\nThe remaining items are: '
        # string of non-key items
        for i in non_key_items:
            sentence += i + ' ' 

        return sentence
        


# Create a class called SpecialDeal that inherits from MealDeal
class SpecialDeal(MealDeal):
# Override the string method so that printing a MealDeal returns
#    You are a special deal winner! Your meal is free!
    def __str__(self):
        return 'You are a special deal winner! Your meal is free!'
