class SimulateWordle:
    def calculateColours(self, word, answer):
        colours = []
        for i in range(len(word)):
            if word[i] == answer[i]:
                colours.append((word[i], i, "Green"))
            elif word[i] not in answer:
                colours.append((word[i], i, "Black"))
            elif self.isYellow(word, answer, i):
                colours.append((word[i], i, "Yellow"))
            else:
                colours.append((word[i], i, "Red"))

        return colours

    def isYellow(self, word, answer, i):
        if word.count(word[i]) > 1:
            if i > word.index(word[i]):
                if answer.count(word[i]) == 1:
                    return False
                else:
                    return True
        return True