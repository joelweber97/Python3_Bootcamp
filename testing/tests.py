import unittest  #import unittest
from activities import eat, nap, is_funny, laugh   #import the functionality we want to test
#in this case we want to test the eat function and nap functions from activities.py


class ActivityTests(unittest.TestCase):  #whatever we want the class to be called. #We have to inherit from TestCase
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat('broccoli', is_healthy = True),
            'Im eating broccoli, because my body is a temple')
            
    def test_eat_unhealthy(self):
        """eat should indicate you've given up on healthy eating"""
        self.assertEqual(eat('pizza', is_healthy = False),
            'Im eating pizza, because YOLO')
            
    def test_eat_healthy_boolean(self):
        """is healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat('pizza', is_healthy = 'who cars')
        
            
            
    def test_short_nap(self):
        """short napes should be refreshing"""
        self.assertEqual(nap(1), 'Im feeling refreshed after my 1 hour nap')
    
    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(nap(3), 'Ugh, I overslept. I didnt mean to nap for 3 hours')
    
    
    def test_is_funny_tim(self):
        """tim is not funny"""
        self.assertEqual(is_funny('tim'), False)
        #self.assertFalse(is_funny('tim'))
        #both of these are relatively the same.
        
        
    def test_is_funny_anyone_else(self):
        """anyone besides tim should be funny"""
        self.assertTrue(is_funny('blue'), 'blue should be funny')
        self.assertTrue(is_funny('tammy'), 'tammy should be funny')
        self.assertTrue(is_funny('sven'), 'sven should be funny')
        #you can have more than 1 assertion in each test case, but you want
        #to make sure they are testing similar things.



    def test_laugh(self):
        """checks to see if result of laugh() is in the tuple"""
        self.assertIn(laugh(), ('lol', 'haha', 'tehe'))        




if __name__ == '__main__':   #if the function is being called from this file run unittest.main()
    unittest.main()
    
    
#python tests.py -v  in terminal
#this will run the tests and print out the docstrings in each function to provide a bit
#more detail when it comes to what we are actually testing.
