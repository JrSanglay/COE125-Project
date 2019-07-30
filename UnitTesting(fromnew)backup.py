# -*- coding: utf-8 -*-
import unittest
#import resources
from DataLogic import Data_Logic


class TestLogin(unittest.TestCase):
    
    #dl = Data_Logic()
    
    def test_UserCheck(self):
        dl = Data_Logic()

        self.assertTrue(dl.UserCheck("bits"))
        self.assertTrue(dl.PasswordCheck("kang123"))
        self.assertTrue(dl.RegUserCheck("Siomai"))

        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
    