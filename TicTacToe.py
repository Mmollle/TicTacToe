#
#   Tic Tac Toe
#
#   To do:
#   Ask the user(s) for and get input about where the user wants to place his X/O
#   Make it impossible to overwrite an already placed X/O
#

import itertools, sys

#table = [[str(i + 1) for x in range(3)] for y in range(3)]
table, i = [], 1
used = [-1]

def main():
    print("Welcome!")
    isRunning = True
    players = ['X', 'O']
    while isRunning == True:
        for player in players:
            printTable()

            correctInput = False
            while correctInput == False:
                if changeTable(input("Where do you want to put '{}'?".format(player)), player) == True:
                    correctInput = True

            if checkWin(player) == True:
                printTable()
                print("The game is won!")
                sys.exit()


for x in range(3):
    for y in range(1):
        table.append([str(i), str(i+1), str(i+2)])
        i = i + 3


# Prints the contents of the list table
def printTable():
    for x in range(3):
        print("  ".join(table[x]))
    print("\n")


# Changes the values of the two-dimensional list
def changeTable(userInput, userSymbol):
    for e, lists in enumerate(table):
        for f, value in enumerate(lists):
            if userInput.isnumeric() and int(userInput) >= 1 and int(userInput) <= 9:
                if userInput == value:
                    table[e][f] = userSymbol
                    return True


# Checks if the game is won
def checkWin(userSymbol):
    isWon, xSumBoolean, ySumBoolean = False, False, False
    xList, yList = [], []

    # Adds X and Y-coordinates for each 'X' found to separate lists (xList and yList)
    for i, x in enumerate(range(3)):
        for j, y in enumerate(range(3)):
            if table[x][y] == userSymbol:
                xList.append(i)
                yList.append(j)

    # Goes through each combination of 3 in xList
    for combinationsX in itertools.combinations(xList, 3):
        if sum(combinationsX) % 3 == 0:
            xSumBoolean = True
    # Goes through each combination of 3 in yList
    for combinationsY in itertools.combinations(yList, 3):
        if sum(combinationsY) % 3 == 0:
            ySumBoolean = True
    # If the sum of the combination of three X/O coordinates in both X and Y directions modulo 3 equals 0, that means its three in a row
    if xSumBoolean == True and ySumBoolean == True:
        return True

if __name__ == "__main__": main()
