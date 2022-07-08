'''
question8_solution.py

Corresponding solution file for question8.py.

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

# Create a class called Trolley with one instance attribute called 'contents'
# that is created in the constructor. 
#     - 'contents' will be a dictionary and will start empty in the constructor
#        but when populated later by other methods: 
#         - the keys will be string describing the product (e.g. 'bread') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'cost' of a single product and 
#                   2. the second item is 'quantity' 
#                   (e.g. {'cost':1.50, 'quantity':3})

class Trolley:
    def __init__(self):
        self. contents = {}

# Create a method called add_product(). It should:
#   - have 3 parameters: 'product_name', 'product_cost' and 'quantity'
#   - 'quantity' has a default value of 1
#   - it should add the product to the 'contents' attribute
#        - if the product exists already, increase the quantity accordingly and ignore
#          the product_cost if different than the one already in the dictionary
#        - if the product does not already exist in the dictionary, add a new entry

    def add_product(self, product_name, product_cost, quantity=1):
        # check if in dict already
        if product_name in self.contents:
            # if is, add quantity to existing entry
            self.contents[product_name]['quantity'] = self.contents[product_name]['quantity'] + quantity
        else:
            # otherwise create new entry
            self.contents[product_name] = {'cost':product_cost, 'quantity':quantity}

# Create a method called remove_product(). It should:
#   - have 1 parameter: 'product_name'
#   - it should remove the product from the 'contents' attribute
#        - if the product exists already, decrease the quantity accordingly
#        - if the product quantity becomes 0, remove the entry from the dictionary

    def remove_product(self, product_name):
        # check if in dict already
        if product_name in self.contents:
            # if is, decreased quantity by 1
            self.contents[product_name]['quantity'] = self.contents[product_name]['quantity'] - 1
            # if quantity now 0, remove product entirely
            if self.contents[product_name]['quantity'] == 0:
                self.contents.pop(product_name)


# Creat a method called calculate_cost(). It should:
#   - return the total value of the trolley (cost x quantity)
    def calculate_cost(self):
        sum = 0
        for product in self.contents.values():
            sum = sum + product['cost'] * product['quantity']
        return sum


