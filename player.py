import time
import solver.wordList as wordList
import solver.strategies as strategy
import solver.masterWordList as masterWordList
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class player:
    def openBrowser(self):
        driver = webdriver.Chrome()
        driver.get("https://www.powerlanguage.co.uk/wordle/")
        return driver

    def enterWord(self, driver, currentWord):
        time.sleep(1)
        page = driver.find_element(By.TAG_NAME, 'html')
        page.click()
        page.send_keys(currentWord)
        page.send_keys(Keys.ENTER)
        time.sleep(1)

    def getResults(self, driver, guessNumber):
        gameApp = driver.find_element(By.TAG_NAME, "game-app")
        game = driver.execute_script("return arguments[0].shadowRoot.getElementById('game')", gameApp)
        gameBoard = game.find_element(By.ID, "board")
        rows = driver.execute_script("return arguments[0].getElementsByTagName('game-row')", gameBoard)
        row = driver.execute_script("return arguments[0].shadowRoot.querySelector(""'.row').innerHTML", rows[guessNumber-2])

        return row

    def parsedRow(self, row):
        soup = BeautifulSoup(row, features="html.parser")

        colourCoded = []
        position = 0
        for tile in soup.find_all('game-tile'):
            colourCoded.append((tile.get('letter'), position, tile.get('evaluation')))
            position += 1
        
        return colourCoded

    def createKnowledge(self, correct, present, absent, doubles, colours, currentWord):
        for item in colours:
            if item[2] == "correct":
                if (item[0], item[1]) not in correct:
                    correct.append((item[0], item[1]))
            elif item[2] == "present":
                if (item[0], item[1]) not in present:
                    present.append((item[0], item[1]))
            elif item[2] == "absent":
                if currentWord.count(item[0]) > 1:
                    matchedLetters = [x for x in colours if x[0] == item[0]]
                    if matchedLetters[0][2] == "absent" and matchedLetters[1][2] == "absent":
                        if item[0] not in absent:
                            absent.append(item[0])
                    else: # item[2] == "Red"
                        if item[0] not in doubles:
                            doubles.append(item[0])
                        if (item[0], item[1]) not in present:
                            present.append((item[0], item[1]))  #not sure about this
                else:
                    if item[0] not in absent:
                            absent.append(item[0])

        print(correct, present, absent, doubles)
        return correct, present, absent, doubles

    def playGame(self):
        masterList = masterWordList.MasterWordList()
        wordleWordList = wordList.WordList()
        strategies = strategy.Strategies()
        correct, present, absent, doubles, = [], [], [], []
        guess = "stern"
        secondGuess = "audio"

        masterWordleList = masterList.createWordList()
        words = masterWordleList

        triedMatchCatch = False

        driver = wordlePlayer.openBrowser()

        for guessNumber in range(2,7):
            self.enterWord(driver, guess)
            row = self.getResults(driver, guessNumber)
            colours = self.parsedRow(row)

            if (colours[0][2] == 'correct' and
                colours[1][2] == 'correct' and
                colours[2][2] == 'correct' and
                colours[3][2] == 'correct' and
                colours[4][2] == 'correct'):
                    print("Congratulations you won")
                    time.sleep(10)
                    return True

            correct, present, absent, doubles = self.createKnowledge(correct, present, absent, doubles, colours, guess)
            words = wordleWordList.createWordList(words, correct, present, absent, doubles, guess)
            guess, triedMatchCatch = strategies.chooseWord(words, correct, present, guessNumber, masterWordleList, triedMatchCatch, secondGuess)
            print(colours)

            time.sleep(1)
        return False

if __name__ == '__main__':
    wordlePlayer = player() 
    wordlePlayer.playGame()  