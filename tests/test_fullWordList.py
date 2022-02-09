import unittest
import sys
sys.path.insert(0, '/Projects/Python/WordleSolver')
from main import app
import solver.masterWordList as masterWordList

class TestFullWordList(unittest.TestCase):
    def test_fullWordList(self):
        print("Running test...")
        
        masterList = masterWordList.MasterWordList()
        words = masterList.createWordList()
        successes = 0
        guessDistribution = [0,0,0,0,0,0]

        startWord = [ str(x) for x in "stern" ]
        secondGuess = [ str(x) for x in "audio" ]

        for word in words:
            if word[0] == startWord:
                successes += 1
                guessDistribution[0] += 1
            else:
                response = app.application(self, startWord, word[0], secondGuess, False)
                if response != -1:
                    successes += 1
                    guessDistribution[response-1] += 1

        print(f"Successes {successes}")
        print(f"Fails {len(words) - successes}")
        print(f"Success rate {int((successes/len(words))*100)}%")
        print("Guess Distribution")
        for x in range(6):
            print(f"{x+1} - {guessDistribution[x]}")

if __name__ == "__main__":
    unittest.main()