from project02part3 import us15_check_lesserthan_15siblings
import unittest
from collections import defaultdict
import datetime
class TestProject(unittest.TestCase):

    def test_check_15siblings(self):
        self.assertTrue(us15_check_lesserthan_15siblings('sibling_1.ged'))
    def test_check_15siblings1(self):
        self.assertTrue(us15_check_lesserthan_15siblings('sibling_2.ged'))


if __name__=='__main__':
 unittest.main()
