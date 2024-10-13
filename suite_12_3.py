import tests_12_2
import tests_12_1
import unittest

TourST = unittest.TestSuite()
TourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TourST)