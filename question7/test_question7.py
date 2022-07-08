'''
test_question7.py

Unit tests for question 7.
'''

import unittest
import question7 as q

class TestQuestion7(unittest.TestCase):
    def test_meal_constructor(self):
        '''
        Test meal with default values
        '''
        result = q.MealDeal(meal_type='hot', items=['soup', 'bread', 'tea', 'banana'])
        self.assertEqual(result.meal_type, 'hot')
        self.assertDictEqual(q.MealDeal.meal_options, {'hot':['soup', 'panini'], 
                    'cold':['sandwich', 'salad']})
    
    def test_meal_constructor_error(self):
        '''
        Test meal with invalid values
        '''
        with self.assertRaises(ValueError):
            result = q.MealDeal('market', ['soup', 'bread', 'tea', 'banana'])
    

    def test_valid_odd_number(self):
        '''
        Test for valid deal with 5 items
        '''
        result = q.MealDeal('cold', ['crisps', 'soda', 'sandwich', 'apple', 'cookie'])
        self.assertFalse(result.is_valid_meal())
    
    def test_valid_4(self):
        '''
        Test for valid meal deal
        '''
        result = q.MealDeal('cold', ['crisps', 'soda', 'sandwich', 'apple'])
        self.assertTrue(result.is_valid_meal())
        self.assertListEqual(result.items, ['crisps', 'soda', 'sandwich', 'apple'])
    
    def test_invalid_item_type(self):
        '''
        Test for invalid meal deal with mismatch of meal type and key item
        '''
        result = q.MealDeal('hot', ['crisps', 'soda', 'sandwich', 'apple'])
        self.assertFalse(result.is_valid_meal())
        self.assertListEqual(result.items, ['crisps', 'soda', 'sandwich', 'apple'])

    def test_valid_8(self):
        '''
        Test for valid meal deal with 8 items
        '''
        result = q.MealDeal('cold', ['crisps', 'soda', 'sandwich', 'apple', 
                                     'sandwich', 'water', 'banana', 'cookie'])
        self.assertTrue(result.is_valid_meal())
    
    def test_invalid_5(self):
        '''
        Test for invalid meal deal with 5 items
        '''
        result = q.MealDeal('cold', ['soda', 'sandwich', 'apple', 'cookie', 'crisps'])
        self.assertFalse(result.is_valid_meal())

    def test_print(self):
        '''
        Test printing the meal
        '''
        result = q.MealDeal('cold', ['soda', 'sandwich', 'apple'])
        str_result = str(result)
        self.assertEqual(str_result, 'The meal contains 1 cold items: sandwich \nThe remaining items are: soda apple ')


    def test_super_print(self):
        '''
        Test printing the super deal
        '''
        result = q.SpecialDeal('hot', ['panini', 'apple'])
        str_result = str(result)
        self.assertEqual(str_result, 'You are a special deal winner! Your meal is free!')
 
if __name__ == '__main__':
    unittest.main()