"""
Should be in tests folder, but I'm having trouble with the path
"""

import unittest

import setstate as ss

class TestStateOfList(unittest.TestCase):
    def test_set_empty(self):
        """ fail set exist; no other state checks """
        a_list = [1]
        a_set = set([])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,-999)

    def test_list_empty(self):
        """ fail list exist; no other state checks """
        a_list = []
        a_set = set([1])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,0)

    def test_set_allduplicates_allmissing_allunexpected(self):
        """ pass exist, fail unique, fail expected(missing&unexpected) """
        a_list = [1,1,2,2]
        a_set = set([5])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,100)

    def test_list_noduplicates_allmissing_allunexpected(self):
        """ pass exist, pass only unique, fail expected(missing&unexpected) """
        a_list = [1,2]
        a_set = set([5])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,110)

    def test_list_someduplicates_allmissing_allunexpected(self):
        """ pass exist, fail only unique, fail expected(missing&unexpected) """
        a_list = [1,1,2]
        a_set = set([5])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,120)

    def test_set_allduplicates_nomissing_nounexpected(self):
        """ pass exist, fail unique, pass expected """
        a_list = [1,1,2,2]
        a_set = set([1,2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,101)

    def test_list_noduplicates_nomissing_noexpected(self):
        """ pass exist, pass only unique, pass expected """
        a_list = [1,2]
        a_set = set([1,2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,111)

    def test_list_someduplicates_nomissing_nounexpected(self):
        """ pass exist, fail only unique, pass expected """
        a_list = [1,1,2]
        a_set = set([1,2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,121)

    def test_set_allduplicates_somemissing_nounexpected(self):
        """ pass exist, fail unique, fail expected(missing) """
        a_list = [1,1,2,2]
        a_set = set([1,2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,102)

    def test_list_noduplicates_somemissing_nounexpected(self):
        """ pass exist, pass only unique, fail expected(missing) """
        a_list = [1,2]
        a_set = set([1,2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,112)

    def test_list_someduplicates_somemissing_nounexpected(self):
        """ pass exist, fail only unique, fail expected(missing) """
        a_list = [1,1,2]
        a_set = set([1,2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,122)

    def test_set_allduplicates_somemissing_someunexpected(self):
        """ pass exist, fail unique, fail expected(missing&unexpected) """
        a_list = [1,1,2,2]
        a_set = set([2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,103)

    def test_list_noduplicates_somemissing_someunexpected(self):
        """ pass exist, pass only unique, fail expected(missing&unexpected) """
        a_list = [1,2]
        a_set = set([2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,113)

    def test_list_someduplicates_somemissing_someunexpected(self):
        """ pass exist, fail only unique, fail expected(missing&unexpected) """
        a_list = [1,1,2]
        a_set = set([2,3])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,123)

    def test_set_allduplicates_nomissing_someunexpected(self):
        """ pass exist, fail unique, fail expected(unexpected) """
        a_list = [1,1,2,2]
        a_set = set([2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,104)

    def test_list_noduplicates_nomissing_someunexpected(self):
        """ pass exist, pass only unique, fail expected(unexpected) """
        a_list = [1,2]
        a_set = set([2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,114)

    def test_list_someduplicates_nomissing_someunexpected(self):
        """ pass exist, fail only unique, fail expected(unexpected) """
        a_list = [1,1,2]
        a_set = set([2])
        result = ss.state_of_list(a_list,a_set)
        self.assertEqual(result,124)

if __name__ == '__main__':
    unittest.main()
