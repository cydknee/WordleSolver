import unittest
import sys
sys.path.insert(0, '/Projects/Python/WordleSolver')
from main import app

class TestSingleWords(unittest.TestCase):
    def setUp(self):
        super(TestSingleWords, self).setUp()
        self.startWord = [ str(x) for x in "stern" ]
        self.secondGuess = [ str(x) for x in "audio" ]
    
    def tearDown(self):
        super(TestSingleWords, self).tearDown()
        self.startWord = []

    def test_singleWord_wooer(self):
        answer =  [ str(x) for x in "wooer" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")
        
    def test_singleWord_hatch(self):
        answer =  [ str(x) for x in "hatch" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")
    
    def test_singleWord_boxer(self):
        answer =  [ str(x) for x in "boxer" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_verge(self):
        answer =  [ str(x) for x in "verge" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_wafer(self):
        answer =  [ str(x) for x in "wafer" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_tight(self):
        answer =  [ str(x) for x in "tight" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_mower(self):
        answer =  [ str(x) for x in "mower" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_golly(self):
        answer =  [ str(x) for x in "golly" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

    def test_singleWord_willy(self):
        answer =  [ str(x) for x in "willy" ]

        response = app.application(self, self.startWord, answer, self.secondGuess, True)
        self.assertGreater(response, 0, f"Should be 1 to 6, but was {response}")

if __name__ == "__main__":
    unittest.main()