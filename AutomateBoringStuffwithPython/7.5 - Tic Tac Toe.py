'''
    This is a simple tic tac toe game using basic python (without any helper modules, aside from os)
    This game is made based on Automate The Boring Stuff with Python Course with slight changes
    Implements Dictionary, Basic Functions, Built-in String Functions, and simple Selection and Repetition
'''
from os import system,name

# Utility Code

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Game Functions

board = {'top-left':' ', 'top-mid':' ', 'top-right':' ', 
         'mid-left':' ', 'mid':' ', 'mid-right':' ',
         'bottom-left':' ', 'bottom-mid':' ', 'bottom-right':' '}

def initBoard():
    board['top-left'], board['top-mid'], board['top-right'] = ' ', ' ', ' '
    board['mid-left'], board['mid'], board['mid-right'] = ' ', ' ', ' '
    board['bottom-left'], board['bottom-mid'], board['bottom-mid'] = ' ', ' ', ' '

def printBoard():
    print(" ___________")
    print("|   |   |   |  Location Details")
    print("| " + board['top-left'] + ' | ' + board['top-mid']+ ' | ' + board['top-right'] + ' |  ------------------------------------------')
    print("|___|___|___|  |  top-left   |   top-mid  |  top-right  |")
    print("|   |   |   |  ------------------------------------------")
    print("| " + board['mid-left'] + ' | ' + board['mid']+ ' | ' + board['mid-right'] + ' |  |  mid-left   |     mid    |  mid-right  |')
    print("|___|___|___|  ------------------------------------------")
    print("|   |   |   |  | bottom-left | bottom-mid | bottom-right|")
    print("| " + board['bottom-left'] + ' | ' + board['bottom-mid']+ ' | ' + board['bottom-right'] + ' |  ------------------------------------------')  
    print("|___|___|___|  ")

def checkBoard(player):
    #check horizontal
    if board['top-left'] == board['top-mid'] == board['top-right'] == player:
        return True
    elif board['mid-left'] == board['mid'] == board['mid-right'] == player:
        return True
    elif board['bottom-left'] == board['bottom-mid'] == board['bottom-right'] == player:
        return True
    #check vertical
    elif board['top-left'] == board['mid-left'] == board['bottom-left'] == player:
        return True
    elif board['top-mid'] == board['mid'] == board['bottom-mid'] == player:
        return True
    elif board['top-right'] == board['mid-right'] == board['bottom-right'] == player:
        return True
    #check diagonal
    elif board['top-left'] == board['mid'] == board['bottom-right'] == player:
        return True
    elif board['top-right'] == board['mid'] == board['bottom-left'] == player:
        return True
    else:
        return False

def checkDraw():
    if ' ' in board.values():
        return False
    else:
        return True

def validMove(location):
    if board[location]==' ':
        return True
    else:
        return False

def startGame():
    clear()
    initBoard()
    player1,player2 = {"symbol":'X'}, {"symbol":'O'}
    player1['name'] = str(input("Insert Player 1's Name [X]: ")).strip().capitalize()
    player2['name'] = str(input("Insert Player 2's Name [O]: ")).strip().capitalize()
    while True:
        while True:
            clear()
            print("It's "+player1['name']+'\'s turn!')
            printBoard()
            move = str(input(player1['name']+'\'s move['+player1['symbol']+']: '))
            board.setdefault(move, None)
            if validMove(move):
                board[move] = player1['symbol']
                break
            else:
                print("Invalid Move")
                input()
        if checkBoard(player1['symbol']):
            print(player1['name']+' wins!!')
            printBoard()
            break
        elif checkDraw():
            print("It's a Draw!!")
            printBoard()
            break
        while True:   
            clear()
            print("It's "+player2['name']+'\'s turn!')   
            printBoard()
            move = str(input(player2['name']+'\'s move['+player2['symbol']+']: '))
            board.setdefault(move, None)
            if validMove(move):
                board[move] = player2['symbol']
                break
            else:
                print("Invalid Move")
                input()
        if checkBoard(player2['symbol']):
            print(player2['name']+' wins!!')
            printBoard()
            break
        elif checkDraw():
            print("It's a Draw!!")
            printBoard()
            break
    input("Press enter to continue..")
    
# Driver Code
while True:
    clear()
    print("Tic Tac Toe Game")
    print("  Input \'Play\' to start game...")
    print("  Input \'Exit\' to quit game")
    menu = str(input(">> "))
    if menu.lower()=='play':
        startGame()
    elif menu.lower() =='exit':
        break