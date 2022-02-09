class MasterWordList:
    def importWordList(self):
        with open('wordleAnswers.txt') as file:
            wordList = [[ str(x) for x in i ] for i in file.read().splitlines() ]

        return wordList

    def calulateScoreForWord(self, word):
        topTierLetters = ['e','a','r','o','t']
        secondTierLetters = ['l','i','s','n','c']
        thirdTierLetters = ['u','y','d','h','p']
        fourthTierLetters = ['m','g','b','f','k']



        score = 0
        for letter in topTierLetters:
            if letter in word:
                score += 1

        for letter in secondTierLetters:
            if letter in word:
                score += 0.5

        for letter in thirdTierLetters:
            if letter in word:
                score += 0.25
        
        # for letter in fourthTierLetters:
        #     if letter in word:
        #         score += 0.1

        return score

    def addScoreToWords(self, wordList):
        wordAndScoreList = []

        for word in wordList:
            wordAndScoreList.append((word, self.calulateScoreForWord(word)))

        return wordAndScoreList

    def createWordList(self):
        return self.addScoreToWords(self.importWordList())