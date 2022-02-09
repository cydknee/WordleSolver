import solver.masterWordList as masterWordList
import solver.simulateWordle as wordle
import solver.knowledge as knowledge
import solver.wordList as wordList
import solver.strategies as strategy

class app:
    def application(self, guess, answer, secondGuess, debug):
        masterList = masterWordList.MasterWordList()
        simulateWordle = wordle.SimulateWordle()
        knownInfo = knowledge.Knowledge()
        wordleWordList = wordList.WordList()
        strategies = strategy.Strategies()

        correct, present, absent, doubles = [], [], [], []
        triedMatchCatch = False

        masterWordleList = masterList.createWordList()
        words = masterWordleList

        for numberOfGuesses in range(2,7):
            colours = simulateWordle.calculateColours(guess, answer)
            correct, present, absent, doubles = knownInfo.createKnowledge(correct, present, absent, doubles, colours)
            words = wordleWordList.createWordList(words, correct, present, absent, doubles, guess)
            guess, triedMatchCatch = strategies.chooseWord(words, correct, present, numberOfGuesses, masterWordleList, triedMatchCatch, secondGuess)

            if guess == answer:
                if debug:
                    print("guess", numberOfGuesses, "".join(guess))
                    print("you won, answer is", "".join(guess), numberOfGuesses,"/ 6")
                return numberOfGuesses
            else:
                if debug:
                    print("guess", numberOfGuesses, "".join(guess))

        
        print(answer)
        return -1

if __name__ == '__main__':
    startWord = [ str(x) for x in "stern" ]
    secondGuess = [ str(x) for x in "audio" ]
    answer = [ str(x) for x in "staff" ]
    mainApp = app()
    guesses = mainApp.application(startWord, answer, secondGuess, False)
    if guesses != -1:
        print(f'You won, answer is {"".join(answer)} {guesses}/ 6')