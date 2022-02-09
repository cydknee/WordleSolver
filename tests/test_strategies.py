import unittest
import sys
sys.path.insert(0, '/Projects/Python/WordleSolver')
import solver.strategies as strategy
import solver.masterWordList as masterWordList

class TestStrategies(unittest.TestCase):
    def test_rejectDoubleLetters_useNewWordList(self):
        words = [(['s', 't', 'o', 'o', 'l'], 3.0), (['s', 't', 'a', 'f', 'f'], 2.5), (['s', 't', 'o', 'u', 't'], 2.5), (['s', 't', 'a', 'l', 'k'], 3.0), (['s', 't', 'o', 'm', 'p'], 2.5), (['s', 't', 'i', 'c', 'k'], 2.5), (['s', 't', 'u', 'c', 'k'], 2.0), (['s', 't', 'u', 'd', 'y'], 1.5), (['s', 't', 'a', 'c', 'k'], 3.0), (['s', 't', 'a', 'm', 'p'], 2.5), (['s', 't', 'i', 'l', 'l'], 2.5), (['s', 't', 'o', 'o', 'd'], 2.5), (['s', 't', 'i', 'l', 't'], 2.5), (['s', 't', 'o', 'c', 'k'], 3.0), (['s', 't', 'o', 'i', 'c'], 3.5), (['s', 't', 'u', 'm', 'p'], 1.5), (['s', 't', 'i', 'f', 'f'], 2.0), (['s', 't', 'a', 'l', 'l'], 3.0), (['s', 't', 'u', 'f', 'f'], 1.5), (['s', 't', 'a', 's', 'h'], 2.5), (['s', 't', 'o', 'o', 'p'], 2.5), (['s', 't', 'a', 'i', 'd'], 3.0)]
        strategies = strategy.Strategies
        guess = strategies.rejectDoubleLetters(self, words)
        self.assertEqual(['s', 't', 'a', 'l', 'k'], guess, f"Should be ['s', 't', 'a', 'l', 'k'], but was {guess}")

    def test_rejectDoubleLetters_useWordList(self):
        words = [(['s', 't', 'o', 'o', 'l'], 3.0), (['s', 't', 'a', 'f', 'f'], 2.5), (['s', 't', 'o', 'u', 't'], 2.5), (['s', 't', 'i', 'l', 'l'], 2.5), (['s', 't', 'o', 'o', 'd'], 2.5), (['s', 't', 'i', 'l', 't'], 2.5), (['s', 't', 'i', 'f', 'f'], 2.0), (['s', 't', 'a', 'l', 'l'], 3.0), (['s', 't', 'u', 'f', 'f'], 1.5), (['s', 't', 'a', 's', 'h'], 2.5), (['s', 't', 'o', 'o', 'p'], 2.5)]
        strategies = strategy.Strategies
        guess = strategies.rejectDoubleLetters(self, words)
        self.assertEqual(['s', 't', 'o', 'o', 'l'], guess, f"Should be ['s', 't', 'o', 'o', 'l'], but was {guess}")

    def test_sortHighestScore(self):
        unsortedwords = [(['s', 't', 'o', 'o', 'l'], 3.0), (['s', 't', 'a', 'f', 'f'], 2.5), (['s', 't', 'o', 'u', 't'], 2.5), (['s', 't', 'i', 'l', 'l'], 1.5), (['s', 't', 'o', 'o', 'd'], 4.0)]
        sorted = [(['s', 't', 'o', 'o', 'd'], 4.0), (['s', 't', 'o', 'o', 'l'], 3.0), (['s', 't', 'a', 'f', 'f'], 2.5), (['s', 't', 'o', 'u', 't'], 2.5), (['s', 't', 'i', 'l', 'l'], 1.5)]
        strategies = strategy.Strategies
        guess = strategies.sortHighestScore(self, unsortedwords)
        self.assertEqual(sorted, guess, f"Should be {sorted}, but was {guess}")

    # def test_hatchMatchCatch(self):
    #     words = [(['h', 'a', 't', 'c', 'h'], 3.0), (['m', 'a', 't', 'c', 'h'], 2.5), (['c', 'a', 't', 'c', 'h'], 2.5), (['l', 'a', 't', 'c', 'h'], 2.5), (['p', 'a', 't', 'c', 'h'], 2.5), (['b', 'a', 't', 'c', 'h'], 2.5), (['w', 'a', 't', 'c', 'h'], 2.5)]
    #     strategies = strategy.Strategies
    #     masterList = masterWordList.MasterWordList()
    #     masterWords = masterList.createWordList()
    #     guess = strategies.hatchMatchCatch(self, words, [('a', 1), ('t', 2), ('c', 3), ('h', 4)], 2, masterWords)
    #     self.assertEqual(['w', 'h', 'e', 'l', 'p'], guess, f"Should be ['w', 'h', 'e', 'l', 'p'], but was {guess}")

if __name__ == "__main__":
    unittest.main()