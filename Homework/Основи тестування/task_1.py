# Task 1

# Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. 

from practice_07_18_1 import Movie
import unittest

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.instance1=Movie("Titanic", "Cameron", "Drama", 1997, "2:45", 9)
    def test_update_info(self):
        self.instance1.update_info("Skazhene Vesilla", "Cameron", "Drama", 1997, "2:45", 9)
        expected_attributes = ("Skazhene Vesilla", "Cameron", "Drama", 1997, "2:45", 9)

        self.assertEqual(self.instance1.title, expected_attributes[0])
        self.assertEqual(self.instance1.director, expected_attributes[1])
        self.assertEqual(self.instance1.genre, expected_attributes[2])
        self.assertEqual(self.instance1.year, expected_attributes[3])
        self.assertEqual(self.instance1.dur, expected_attributes[4])
        self.assertEqual(self.instance1.rate, expected_attributes[5])

if __name__ == "__main__":
    unittest.main()