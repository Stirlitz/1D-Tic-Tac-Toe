#Peter Fajner
#2014-06-23

import os
clear = lambda: os.system('clear')

def winCondition():
    condition = '' 
    check = 10
    for j in range(0, 9):
        if board[j] != '-' and (j+1) %3 == 0 and board[j] == board[j+3] == board[j+6]:
            condition = True
            return j
            break
        if board[j] != '-' and (j+1) %3 == 0 and board[j] == board[j+3] == board[j+6]:
            condition = True
            check = 2
            return j
            break
        if board[0] != '-' and board[0] == board[4] == board[8]:
            condition = True
            check = 3
            return 0
            break
        if board[2] != '-' and board[2] == board[4] == board[6]:
            condition = True
            check = 4
            return 2
            break
    return winner
    #return check

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
key = "7 8 9\n4 5 6\n1 2 3"

winner = 10
move = 1
player = 'X'
condition = False
message = ''
while winner == 10:
    move = move * -1
    if move == 1: player = 'X'
    if move == -1: player = 'O'
    winner = winCondition()
    if winner != 10: break
    clear()
    #check = winCondition()
    #print check
    #print condition
    print message
    print key, '\n'
    print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
    nextMove = int(raw_input(player + ": Pick a space "))
    print '\n'
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

clear()
print ''
print key, '\n'
print board[6], board[7], board[8], '\n', board[3], board[4], board[5], '\n', board[0], board[1], board[2], '\n'
print 'Game over!', board[winner], 'wins!\n'


