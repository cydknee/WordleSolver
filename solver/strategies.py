class Strategies:
    def chooseWord(self, wordList, correct, present, numberOfGuesses, masterWordList, triedMatchCatch, secondGuessWord):
        if (len(correct) == 0 and len(present) < 2) and numberOfGuesses == 2:
            return secondGuessWord, triedMatchCatch
        elif self.shouldUseMatchCatch(correct, numberOfGuesses, triedMatchCatch, len(wordList)):
            triedMatchCatch = True
            return self.hatchMatchCatch(wordList, masterWordList), triedMatchCatch
        else:
            # if list(filter(lambda x:x[0] == 'r' , present)) and list(filter(lambda x:x[0] == 'e', present)):
            #     wordList = self.erNotRe(wordList)
            return self.rejectDoubleLetters(self.sortHighestScore(wordList)), triedMatchCatch

    def shouldUseMatchCatch(self, correct, numberOfGuesses, triedMatchCatch, wordListLength):
        if (len(correct) == 4 
            and correct[0][1] != 0 
            and correct[1][1] != 0 
            and correct[2][1] != 0 
            and correct[3][1] != 0 
            and (wordListLength >= (6 - numberOfGuesses)) 
            and numberOfGuesses != 6
            and not triedMatchCatch):
                return True
        else:
            return False

    def rejectDoubleLetters(self, wordList):
        newWordList = []
        for word in wordList:
            discardWord = False
            for letter in word[0]:
                if word[0].count(letter) > 1:
                    discardWord = True

            if not discardWord:
                newWordList.append(word)

        if len(newWordList) != 0:
            return newWordList[0][0]
        else:
            return wordList[0][0]

    def sortHighestScore(self, wordlist):
        return sorted(wordlist, key=lambda x:x[1], reverse=True)

    def hatchMatchCatch(self, wordList, masterWordList):
        startingLetters = []
        newWordList = []

        for word in wordList:
            startingLetters.append(word[0][0])

        for word in masterWordList:
            score = 0
            for letter in startingLetters:
                if letter in word[0]:
                    score += 1
            newWordList.append((word, score))

        sortedList = sorted(newWordList, key=lambda x:x[1], reverse=True)
        return sortedList[0][0][0]

    def erNotRe(self, wordList):
        newWordList = []

        for word in wordList:
            if ("".join(word[0]).endswith('er')):
                newWordList.append((word[0], word[1]+5))
            else:
                newWordList.append(word)
        
        return newWordList

