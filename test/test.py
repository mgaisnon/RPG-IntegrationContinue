import unittest

class TestEnvironnement(unittest.TestCase):
    def test_true_est_true(self):
        self.assertTrue(True)

    def testfailure(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
