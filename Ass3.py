from project02part3 import us01_check_dates_before_current_date, us02_check_birth_before_marriage
import unittest
from collections import defaultdict
import datetime
class TestProject(unittest.TestCase):

    def test_birth_date(self):
        self.assertTrue(us01_check_dates_before_current_date('birth.ged'))
    def test_Future_birth(self):
        self.assertFalse(us01_check_dates_before_current_date('Future birthdate.ged'))
    def test_Future_death(self):
        self.assertFalse(us01_check_dates_before_current_date('Future deathdate.ged'))
    def test_Future_Marriagedate(self):
        self.assertFalse(us01_check_dates_before_current_date('Future Marriagedate.ged'))
    def test_deathdate(self):
        self.assertTrue(us01_check_dates_before_current_date('dead.ged'))
    def test_marriagedate(self):
        self.assertTrue(us02_check_birth_before_marriage('BirthbeforeMarriage.ged'))


if __name__=='__main__':
 unittest.main()
