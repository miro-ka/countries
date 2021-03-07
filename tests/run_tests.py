import unittest
import logging
from tests.utils_test import RestCountriesUtilsTest


def test_suite():
    suite = unittest.TestSuite()

    # restcountries Tests
    suite.addTest(RestCountriesUtilsTest('km2_to_miles2_test'))

    return suite


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    runner = unittest.TextTestRunner()
    runner.run(test_suite())
