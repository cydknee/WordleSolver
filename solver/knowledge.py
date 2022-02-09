class Knowledge:
    def createKnowledge(self, correct, present, absent, doubles, colours):
        for item in colours:
            if item[2] == "Green":
                if (item[0], item[1]) not in correct:
                    correct.append((item[0], item[1]))
            elif item[2] == "Yellow":
                if (item[0], item[1]) not in present:
                    present.append((item[0], item[1]))
            elif item[2] == "Black":
                if item[0] not in absent:
                    absent.append(item[0])
            else: # item[2] == "Red"
                if item[0] not in doubles:
                    doubles.append(item[0])

        return correct, present, absent, doubles