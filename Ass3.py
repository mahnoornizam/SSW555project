from project02part3 import us05_check_marriage_before_death, us04_check_marriage_before_divorce
import unittest
from collections import defaultdict
import datetime
class TestProject(unittest.TestCase):

    def test_divorcedate(self):
        self.assertTrue(us04_check_marriage_before_divorce('Marriagebfdivorce.ged'))
    def test_marriagebfdeath(self):
        self.assertTrue(us05_check_marriage_before_death('Marriedbfdeath.ged'))
    def test_marriagebfdeath_1(self):
        self.assertTrue(us05_check_marriage_before_death('Marriedandliving.ged'))


if __name__=='__main__':
 unittest.main()
