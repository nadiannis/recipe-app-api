'''
Sample Tests
'''

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    ''' Test the calc module '''

    def test_add_numbers(self):
        res = calc.add(7, 5)

        self.assertEqual(res, 12)
