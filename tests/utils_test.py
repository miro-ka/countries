import unittest

import restcountries.utils as country_utils


class RestCountriesUtilsTest(unittest.TestCase):

    def km2_to_miles2_test(self):
        km2 = 10.5
        res = country_utils.km2_to_miles2(km2)

        self.assertEqual(res, 4.0540726695)
