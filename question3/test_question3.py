'''
test_question3.py

Unit tests for question 3.
'''

import unittest
import question3 as q

class TestQuestion3(unittest.TestCase):
    def test_attributes(self):
        '''
        Test setting attributes
        '''
        result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
        self.assertListEqual(result.front_chainring_values, [34, 50])

    def test_gear_inches(self):
        '''
        Test calculating gear inches
        '''
        result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
        self.assertAlmostEqual(result.get_gear_inches(), 32.79, places=2)

    def test_single_speed_true(self):
        '''
        Test that identifies is a single speed bike
        '''
        result = q.Bicycle([50], [19])
        self.assertTrue(result.is_single_speed())
    
    def test_single_speed_false(self):
        '''
        Test that identifies is not a single speed bike
        '''
        result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
        self.assertFalse(result.is_single_speed())
    
    def test_set_rear_valid(self):
        '''
        Test that rear is set with a valid input
        '''
        result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
        result.set_rear_cog(4)
        self.assertEqual(result.current_rear_cog, 4)

    def test_set_rear_invalid(self):
        '''
        Test that rear set with an invalid input raises error
        '''
        with self.assertRaises(ValueError):
            result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
            result.set_rear_cog(-1)
    
    def test_set_front_valid(self):
        '''
        Test that front is set with a valid input
        '''
        result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
        result.set_front_chainring(2)
        self.assertEqual(result.current_chainring, 2)
        
    def test_set_front_invalid(self):
        '''
        Test that front set with an invalid input raises error
        '''
        with self.assertRaises(ValueError):
            result = q.Bicycle([50, 34], [11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28])
            result.set_front_chainring(4)

    
if __name__ == '__main__':
    unittest.main()