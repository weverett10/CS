'''
Author: Will Everett
Date: 4/7/2026
description: game of mini battleship
Bugs: 
sources: Mr Campbell and Ms. Marciano and Ms. Sharma
'''
import random


def getdots():
    #needs to not return the same 2 numbers

    while True:
    
        columndot = []
        rowdot = []
        
        column += random.randint(0,5)
        row += random.randint

        if len(rowdot) == 4:
            break
        return columndot,rowdot


def checkhit(board1,rowdot,columndot,count):

    if  playermove() == {board1[rowdot][columndot]}:
        {board1[rowdot][columndot]} == '💥'
        return count -1
        
    else:
        {board1[rowdot][columndot]} == '❌'
        pass
        
    
def playermove(playerturn,board1):
    while True:
        while True:
                column = input('which column do you want to put it in? (1 2 3 4 5): ')
                if column != '1' and column != '2' and column != '3' and column != '4' and column != '5':
                    print("Can't do that!!")
                    continue
                
                row = input ('what row do you want to put it in? (1 2 3 4 5): ')
                if row != '1' and row != '2' and row != '3' and row != '4' and row != '5':
                    print (" Can't do that !!!")
                else:
                    break
        


        if board1[int(row)][int(column)-1] == '💧':
            board1[int(row)-1][int(column)-1] = playerturn
            break
        else:
            print("Can't do that!!!")#fix this
            break        
    
def main():
    board1 =   [  
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"]]

    board2 =   [  
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"]]
    
    count = 4

    playerturn = '1'

    if playerturn == '1':
            playerturn = '2'
    else:
            playerturn = '1'


    print(f'''  1   2   3   4   5 
        
1  {board1[0][0]} {board1[0][1]} {board1[0][2]} {board1[0][3]} {board1[0][4]}

2  {board1[1][0]} {board1[1][1]} {board1[1][2]} {board1[1][3]} {board1[1][4]}  
       
3  {board1[2][0]} {board1[2][1]} {board1[2][2]} {board1[2][3]} {board1[2][4]} 

4  {board1[3][0]} {board1[3][1]} {board1[3][2]} {board1[3][3]} {board1[3][4]}          

5  {board1[4][0]} {board1[4][1]} {board1[4][2]} {board1[4][3]} {board1[4][4]}             
                      ''')
    
    playermove(playerturn,board1)
    
    getdots(board1)


    

main()