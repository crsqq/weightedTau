import unittest
from weightedTau import weightedTau, productRS_c

class WeightedTau(unittest.TestCase):
    def test_one(self):
        a = [1,2,3]
        res = weightedTau(a,a)
        self.assertEqual(res, 1)


    def test_medium(self):
        a = [1,2,3,4]
        b = [1,2,4,3]
        res = weightedTau(a,b)
        self.assertEqual(res, 0.52)

    def test_rank(self):
        a = [3, 7, 9, 3, 5]
        b = [11, 6, 6, 3, 5]
        abRank = [3, 1, 0, 4, 2]
        res = productRS_c(a, b, abRank)
        self.assertAlmostEqual(res, 2.01666, places=4)

if __name__ == "__main__":
    unittest.main()
