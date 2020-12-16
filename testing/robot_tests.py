import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    #we can get rid of the need to set mega_man = Robot(...) in each test case by
    #using setUp and tearDown
    def setUp()
    def test_charge(self):
        mega_man = Robot('Mega Man', battery = 50)
        mega_man.charge()
        self.assertEqual(mega_man.battery, 100)
        #this test charges the battery and then tests to make sure the battery
        #is actually set to 100 after the charge
        
    
    def test_say_name(self):
        mega_man = Robot('Mega Man', battery = 50)
        self.assertEqual(mega_man.say_name(), 'BEEP BOOP BEEP BOOP.  I AM MEGA MAN')
        #checks to see if the output from say_name works correctly
        #also want to test to see if battery goes down by 1
        self.assertEqual(mega_man.battery, 49)
        
    def test_say_name2(self):
        mega_man = Robot('Mega Man', battery = 0)
        self.assertEqual(mega_man.say_name(), 'Low power.  Please charge and try again')
        #this test if the charge is 0, say_name should thrown an error.
        
    
    def test_learn_skill(self):
        mega_man = Robot('Mega Man', battery = 50)
        self.assertEqual(mega_man.learn_skill('blowjob', 49), 'WOAH. I KNOW BLOWJOB')
        self.assertEqual(mega_man.battery, 1)
        #test to see if learn_skill will append the 'blowjob' skill to the new skills and 
        #reduce the battery charge by the defined number
        #this only occurs if the battery charge is greater than the cost_to_learn.
        
    def test_learn_skill2(self):
        mega_man = Robot('Mega Man', battery = 50)
        self.assertEqual(mega_man.learn_skill('hj', 51), 'Insufficient battery. Please charge and try again')
        #this tests the outcome when the cost_to_learn a new skill is greater than the current battery charge.

   


if __name__ == '__main__':
    unittest.main()