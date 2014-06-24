#Peter Fajner
#2014-06-23

import os, sys 
clear = lambda: os.system('clear')
key = "7 8 9\n4 5 6\n1 2 3" # a number key that is displayed on the screen

"""Checks whether there is a win condition."""
def winCondition(board):
    for j in range(0, 3):
        if board[j] != '-' and board[j] == board[j+3] == board[j+6]: # vertical line
            return j
        if board[j*3] != '-' and board[j*3] == board[j*3+1] == board[j*3+2]: # horizontal line
            return j
        if board[0] != '-' and board[0] == board[4] == board[8]: # minor diagonal
            return 0
        if board[2] != '-' and board[2] == board[4] == board[6]: # major diagonal
            return 2
    return 10 # default return value if no win condition is found

"""Main game loop."""
def game(winner):
    board = resetBoard() # grabs a fresh board
    move = 1 # alternates between 1 and -1, used to set which player's move it is
    player = 'O' # second player to go
    message = '' # message used to display errors
    while winner == 10:

        # switching between players
        move = move * -1
        if move == 1: player = 'X'
        if move == -1: player = 'O'

        # checks whether there is a win condition, and if there is, ends the game loop
        winner = winCondition(board)
        if winner != 10: continue

        # clears the screen and shows any errors, the key, the game board, and an input prompt
        clear()        
        print message
        print key, '\n'
        print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
        nextMove = raw_input(player + ": Pick a space ")
        print '\n'

        # checks whether input is an integer and is within the correct range and the spot is empty
        try: 
            nextMove = int(nextMove)
            nextMove -= 1 # decrements input by 1, as the program sees the game board as 0-8 rather than 1-9
            if nextMove >= 0 and nextMove <= 8:
                if board[nextMove] == '-':
                    if player == 'X':
                        board[nextMove] = 'X'
                    if player == 'O':
                        board[nextMove] = 'O'
                    message = ''
                else:
                    message = 'Invalid move, go again'
                    move = move * -1
            else:
                message = 'Invalid move, go again'
                move = move * -1
        except ValueError:
            message = 'Invalid move, go again'
            move = move * -1


    # clears the screen and shows any errors, the key, the game board, and the win message
    clear()
    print ''
    print key, '\n'
    print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
    print 'Game over!', board[winner], 'wins!\n'
    next = raw_input("Press Q to quit, any other key to play again. ")
    if next.lower() == 'q':
        sys.exit()

"""Generates a fresh board."""
def resetBoard():
    return ['-', '-', '-', '-', '-', '-', '-', '-', '-']

while True:
    game(10)

