from random import randint

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


def checkWord(guess, word, ans, attempt, wrongGuess):
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                ans[i] = guess
        print(' '.join(ans))

    else:
        if guess not in wrongGuess:
            attempt = attempt - 1

        wrongGuess.add(guess)
        print(f"Your guessed letter {guess} is not in the word")
        print(f"you have {attempt} attempts left")

    if attempt > 0 and '_' in ans:
        guess = guessLetter(len(word))
        checkWord(guess, word, ans, attempt, wrongGuess)


def startGame():
    # randonly selected a word from list
    word = words[randint(0, len(words) - 1)].lower()
    # variable to store
    finalList = list(len(word) * '_')

    print('_ ' * len(word))

    guess = guessLetter(len(word))
    attempt = int(len(word) / 2)
    wrongGuess = {""}

    checkWord(guess, word, finalList, attempt, wrongGuess)

    if '_' not in finalList:
        print("\nYou Win")
    else:
        print("\nYou Lose")


# main--------------------------------------

displayMenu()
choice = chooseOption()

if choice == '1':
    startGame()
else:
    print("Game Over")
