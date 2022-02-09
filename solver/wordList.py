class WordList:
    def createWordList(self, wordList, correct, present, absent, doubles, guess):
        newWordList = []
        
        for wordAndScore in wordList:
            word = wordAndScore[0]
            addToNewList = True
            if guess == word:
                addToNewList = False

            for p in correct:
                if word[p[1]] != p[0]:
                    addToNewList = False   

            for a in present:
                if a[0] not in word or word.index(a[0]) == a[1]:
                    addToNewList = False

            for n in absent:
                if n in word:
                    addToNewList = False

            for d in doubles:
                if word.count(d) > 1:
                    addToNewList = False

            if addToNewList:
                newWordList.append(wordAndScore)

        return newWordList