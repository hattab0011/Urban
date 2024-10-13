import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_walk(self):
        walker = Runner('Max')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_run(self):
        runner = Runner('Dan')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_challenge(self):
        walker = Runner('Max')
        runner = Runner('Dan')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(walker.distance, runner.distance)

