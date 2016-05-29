import unittest
import sys
import search

class Test(unittest.TestCase):
        
	global search_test 
	search_test = search.Search('exemplo1', 'exemplo2')

	def test_Search(self):
		assert isinstance(search_test, search.Search), "search_test should be a Search's instance"
	
	def test_Add(self):
                self.assertEqual(search_test.add(), None)
		
	def test_Query(self):
		assert isinstance(search_test.query(), list), "It should return a list"
	
        def test_Filter(self):
		assert isinstance(search_test.filter(), list), "It should return a list"

if __name__ == "__main__":
	unittest.main()
	import doctest
	doctest.testmod()
