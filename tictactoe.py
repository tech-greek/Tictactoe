# This is a simple TicTacToe game with computer as the second player
import random

board = ['-','-','-',
         '-','-','-',
         '-','-','-']

currentPlayer = "x"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    i = True
    while i:
        inp = int(input("Enter a number between 1 and 9: "))
        if inp>=1 and inp<=9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            i = False
        elif board[inp-1] != "-":
            print("The spot is already taken")
            continue
        else:
            print("Oops wrong number, please enter a number within the range")
            continue

def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!='-':
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!='-':
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!='-':
        winner = board[6]
        return True
    
def checkVeritcal(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner = board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!='-':
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!='-':
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!='-':
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!='-':
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if gameRunning == True:
        if checkDiagonal(board) or checkVeritcal(board) or checkHorizontal(board):
            printBoard(board)
            print(f"The winner is {winner}")
            gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

def computerPlayer(board):
    i = True
    while i:
        inp = random.randint(1,10)
        if inp>=1 and inp<=9 and board[inp-1] == "-":
            board[inp-1] = "o"
            i = False
        else:
            continue
       
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    computerPlayer(board)
    checkWin()
    checkTie(board)
