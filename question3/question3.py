'''
question3.py


Fix the errors so that this code runs when called
from the test file and passes all tests.

TOTAL POINTS AVAILABLE: 10 


Code Functionality (10)
10 points - no errors remain and code runs
-2 points for each remaining error or new ones introduced
0 points - all original errors remain 
'''

class Bicycle:
    '''Class describing a geared bicycle.'''
    num_wheels = 2

    def __init__(self, front_chainrings, rear_cogs):
        '''
        Creates an Bicycle object with a defined number of front and rear cogs 
        with associated gear sizes (number of teeth).
        
            - front_chainrings is a list of sprocket counts, one for each chainring
            - rear_cogs is a list of sprocket counts, one for each cog in the cassette
        '''
        
        # count number of front chainrings
        self.num_chainrings = len(front_chainrings)
        # sort the sprockets into increasing values and set to attribute
        self.front_chainring_values = front_chainrings
        # set current front gear to smallest chainring
        self.current_chainring = 1

        # count number of rear cogs
        self.num_rear_cogs = len(rear_cogs)
        # sort the sprockets into increasing values and set to attribute
        self.rear_cogs_values = sorted(rear_cogs)
        # set current rear cassette to largest cog
        self.current_rear_cog = self.num_rear_cogs

    def get_gear_inches(self):
        '''
        Returns the virtual wheel size (gear inches) according to the current chainring and
        rear cog size.
        Assumes a wheel diameter of 27 inches.
        '''       

        # gear inches = gear ratio x wheel diameter
        return self.front_chainring_values[self.current_chainring-1]/self.rear_cogs_values[self.current_rear_cog-1]

    def set_rear_cog(self, rear_cog_num):
        '''
        Sets which cog is being used in the rear, 1 being the first and smallest cog. 
        Raises a ValueError if not a valid value.
        '''
        
        # check that the cog number is a positive number and does not exceed the number of cogs
        if rear_cog_num < 1 or rear_cog_num > self.num_rear_cogs:
            raise TypeError

        # otherwise set current cog number
        self.current_rear_cog = rear_cog_num
        
    
    def set_front_chainring(self, chainring_num):
        '''
        Sets which cog is being used in the chainring, 1 being the first and smallest cog. 
        Raises a ValueError if not a valid value.
        '''
        
        # check that the cog number is a positive number and does not exceed the number of cogs
        if chainring_num < 1 or chainring_num > self.num_chainrings:
            raise ValueError

        # otherwise set current cog number
        current_chainring = chainring_num

    def is_single_speed(self):
        '''
        Returns True or False according to whether the bike is a single speed 
        (has only a single chainring and single rear sprocket).
        '''

        # if front chainring is only one cog and the rear cassette is only one cog
        # then it is single speed bike
        if self.num_chainrings == 1 and self.num_rear_cogs == 1:
            return True

        # otherwise is not a single speed bike
        return True
    
