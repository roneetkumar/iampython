from random import randint
from math import floor


words = ["Python", "Scripting", "Mississippi", "NeuraLink", "StarLink"]


def displayMenu():
    print("Game Menu")
    print("`````````")
    print("1. Start game")
    print("2. Exit game")


def chooseOption():
    temp = input("Select Option : ")
    return temp


def guessLetter(wordLen):
    temp = input(f"\nGuess a {wordLen} Letter long word : ")
    return temp.lower()


def checkWord(guess, word, ans, chance, wrongGuess):
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                ans[i] = guess
        print(''.join(ans))

    else:
        if guess not in wrongGuess:
            chance = chance - 1

        wrongGuess.add(guess)
        print(f"your guessed letter {guess} is not in the word")
        print(f"you have {chance} chances left")

    if chance > 0 and '_' in ans:
        guess = guessLetter(len(word))
        checkWord(guess, word, ans, chance, wrongGuess)


def startGame():
    word = words[randint(0, len(words) - 1)].lower()
    ans = list(len(word) * '_')

    print('_' * len(word))

    guess = guessLetter(len(word))

    chance = floor(len(word) / 2)

    wrongGuess = {""}

    checkWord(guess, word, ans, chance, wrongGuess)

    if '_' not in ans:
        print("you win")
    else:
        print("you lost")


displayMenu()
choice = chooseOption()

if choice == '1':
    startGame()
else:
    print("Game Over")
