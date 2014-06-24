#Peter Fajner
#2014-06-23

import os, sys 
clear = lambda: os.system('clear')

def winCondition(board):
    condition = '' 
    check = 10
    winner = 10
    for j in range(0, 3):
        if board[j] != '-' and board[j] == board[j+3] == board[j+6]:
            condition = True
            check = 1
            #return check
            return j
            break
        if board[j*3] != '-' and board[j*3] == board[j*3+1] == board[j*3+2]:
            condition = True
            check = 2
            #return check
            return j
            break
        if board[0] != '-' and board[0] == board[4] == board[8]:
            condition = True
            check = 3
            #return check
            return 0
            break
        if board[2] != '-' and board[2] == board[4] == board[6]:
            condition = True
            check = 4
            #return check
            return 2
            break
    return winner
    #return check

def game(winner):
    newBoard = resetBoard()
    board = newBoard
    move = 1
    player = 'X'
    message = ''
    while winner == 10:
        move = move * -1
        if move == 1: player = 'X'
        if move == -1: player = 'O'
        winner = winCondition(board)
        if winner != 10: continue
        clear()
        
        #check = winCondition(board)
        #print check
        
        print message
        print key, '\n'
        print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
        nextMove = raw_input(player + ": Pick a space ")
        print '\n'

        try: 
            nextMove = int(nextMove)
            nextMove -= 1
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


    clear()
    print ''
    print key, '\n'
    print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
    print 'Game over!', board[winner], 'wins!\n'
    next = raw_input("Press Q to quit, any other key to play again. ")
    if next.lower() == 'q':
        sys.exit()

def resetBoard():
    return ['-', '-', '-', '-', '-', '-', '-', '-', '-']


key = "7 8 9\n4 5 6\n1 2 3"

while True:
    game(10)

