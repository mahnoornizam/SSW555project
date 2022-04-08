from project02part3 import us08_check_birth_before_marriage_of_parents, us09_check_birth_before_death_of_parents
import unittest
from collections import defaultdict
import datetime
class TestProject(unittest.TestCase):

    def test_divorcedate(self):
        self.assertTrue(us08_check_birth_before_marriage_of_parents('Birthbfmarriage.ged'))
    def test_marriagebfdeath(self):
        self.assertTrue(us08_check_birth_before_marriage_of_parents('Birthbfmarriage1.ged'))
    def test_marriagebfdeath_1(self):
        self.assertTrue(us09_check_birth_before_death_of_parents('Marriagebfdeath.ged'))


if __name__=='__main__':
 unittest.main()
