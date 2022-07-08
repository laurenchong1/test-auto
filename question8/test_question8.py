'''
test_question8.py

Unit tests for question 8.
'''

import unittest
import question8 as q

class TestQuestion8(unittest.TestCase):
    def test_trolley_constructor_defaults(self):
        '''
        Test Trolley with default values
        '''
        my_trolley = q.Trolley()
        self.assertDictEqual(my_trolley.contents, {})
    
    def test_add_single_product(self):
        '''
        Test adding a new product with the default value
        '''
        my_trolley = q.Trolley()
        my_trolley.add_product('cheese', 1.75)
        self.assertDictEqual(my_trolley.contents, {'cheese':{'cost':1.75, 'quantity':1}})

    def test_add_more(self):
        '''
        Test adding more to an existing product
        '''
        my_trolley = q.Trolley()
        my_trolley.add_product('cheese', 1.75)
        my_trolley.add_product('cheese', 1.75)
        self.assertDictEqual(my_trolley.contents, {'cheese':{'cost':1.75, 'quantity':2}})
    
    def test_decrease_quantity(self):
        '''
        Test decreasing the quantity of a product
        '''
        my_trolley = q.Trolley()
        my_trolley.add_product('cheese', 1.75, quantity=4)
        my_trolley.remove_product('cheese')
        self.assertDictEqual(my_trolley.contents, {'cheese':{'cost':1.75, 'quantity':3}})

    def test_remove_product(self):
        '''
        Test removing an item by decreasing quantity to 0 
        '''
        my_trolley = q.Trolley()
        my_trolley.add_product('cheese', 1.75)
        my_trolley.add_product('eggs', 2.50)
        my_trolley.remove_product('cheese')
        self.assertDictEqual(my_trolley.contents, {'eggs':{'cost':2.5, 'quantity':1}})

    def test_sum(self):
        '''
        Test calculating the total cost of the trolley
        '''
        my_trolley = q.Trolley()
        my_trolley.add_product('cheese', 1.75)
        my_trolley.add_product('eggs', 2.50, 2)
        self.assertEqual(my_trolley.calculate_cost(), 6.75)

 
if __name__ == '__main__':
    unittest.main()