## ex 11.1 and 11.2 city, country, population

import unittest

from city_functions import city_country
# from chapter_11.city_functions import city_country # YOU DONT NEED THIS IF YOU cd to chapter_11 folder!!

class test_city(unittest.TestCase):

    def test_city_country(self):
        """does Santiago, Chile work?"""
        fn_output = city_country('santiago', 'chile')
        self.assertEqual('Santiago, Chile', fn_output)
    

    def test_city_country_population(self):
        """does Santiago, Chile work?"""
        fn_output = city_country('santiago', 'chile', 500000)
        self.assertEqual('Santiago, Chile - Population: 500000', fn_output)

unittest.main()

