'''
question7.py


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

    
# Override the string method so that when printing a meal instance, the text nicely 
# outputs the contents of the meal. 
# Use the format:
#     The meal contains X [hot or cold] items: [item1] [item2] 
#     The remaining items are: [item3] [item4] [item5] [item6]
#  
# Such as:
#    The meal contains 2 hot items: sandwich, panini 
#    The remaining items are crisps, water, apple
 

# Create a class called SpecialDeal that inherits from MealDeal

# Override the string method so that printing a MealDeal returns
#    You are a special deal winner! Your meal is free!