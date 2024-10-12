from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f'Забег {key}: {cls.all_results[key].name}')

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results[max(results.keys())]
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник')

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results[max(results.keys())]
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results[max(results.keys())]
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")


if __name__ == '__main__':
    unittest.main()