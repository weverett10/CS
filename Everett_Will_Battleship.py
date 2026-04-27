'''
Author: Will Everett
Date: 4/7/2026
description: game of mini battleship
Bugs: 
sources: Mr Campbell and Ms. Marciano and Ms. Sharma
'''
import random

def getdots():
    columndot = []
    rowdot = []
    while True:
    
        
        
        column = (random.randint(0,4))
        row = (random.randint(0,4))

        if (row, column) not in zip(rowdot,columndot):
             rowdot.append(row)
             columndot.append(column)

        if len(rowdot) == 4:
            break
    return columndot,rowdot


def checkhit(board1, rowdot, columndot, row, column):
    if board1[row][column] == '💥' or board1[row][column] == '❌':
        print("you already shot there!")
        return False
    elif (row, column) in zip(rowdot, columndot):
        board1[row][column] = '💥'
        print('You Got One!')
        index = list(zip(rowdot, columndot)).index((row, column))
        rowdot.pop(index)
        columndot.pop(index)
        return True

    else:
        board1[row][column] = '❌'
        print('You Missed!')
        return True
        
    
def playermove():
    while True:
            column = int(input('what column would you like to shoot at (1 2 3 4 5): '))
            if column > 0 and column < 6:
                row = int(input('what row would you like to shoot at (1 2 3 4 5): '))
                if row > 0 and row < 6:
                     column = column-1 
                     row = row-1
                     return column,row
                else:
                     print("can't do that try again")
            else:
                 print("can't do that try again")
                

                
def main():
    board1 =   [  
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"],
    ["💧", "💧", "💧", "💧", "💧"]]

    columndot,rowdot = getdots()
    shots = 10


    while shots > 0:

        print(f'''  1   2   3   4   5 
        
1  {board1[0][0]} {board1[0][1]} {board1[0][2]} {board1[0][3]} {board1[0][4]}

2  {board1[1][0]} {board1[1][1]} {board1[1][2]} {board1[1][3]} {board1[1][4]}  
       
3  {board1[2][0]} {board1[2][1]} {board1[2][2]} {board1[2][3]} {board1[2][4]} 

4  {board1[3][0]} {board1[3][1]} {board1[3][2]} {board1[3][3]} {board1[3][4]}          

5  {board1[4][0]} {board1[4][1]} {board1[4][2]} {board1[4][3]} {board1[4][4]}             
                      ''')
       
        print(f'you have{shots} remaining')

        column,row = playermove()
        if checkhit(board1, rowdot, columndot, row, column):
            shots -= 1

        if len(rowdot) == 0:
            print(f'''  1   2   3   4   5 
        
1  {board1[0][0]} {board1[0][1]} {board1[0][2]} {board1[0][3]} {board1[0][4]}

2  {board1[1][0]} {board1[1][1]} {board1[1][2]} {board1[1][3]} {board1[1][4]}  
       
3  {board1[2][0]} {board1[2][1]} {board1[2][2]} {board1[2][3]} {board1[2][4]} 

4  {board1[3][0]} {board1[3][1]} {board1[3][2]} {board1[3][3]} {board1[3][4]}          

5  {board1[4][0]} {board1[4][1]} {board1[4][2]} {board1[4][3]} {board1[4][4]}             
                      ''')
       
            print("you win!!!!🤩")
            break
             
        if shots == 0 and len(rowdot) > 0:
            print(f'''  1   2   3   4   5 
        
1  {board1[0][0]} {board1[0][1]} {board1[0][2]} {board1[0][3]} {board1[0][4]}

2  {board1[1][0]} {board1[1][1]} {board1[1][2]} {board1[1][3]} {board1[1][4]}  
       
3  {board1[2][0]} {board1[2][1]} {board1[2][2]} {board1[2][3]} {board1[2][4]} 

4  {board1[3][0]} {board1[3][1]} {board1[3][2]} {board1[3][3]} {board1[3][4]}          

5  {board1[4][0]} {board1[4][1]} {board1[4][2]} {board1[4][3]} {board1[4][4]}             
                      ''')
       
            print('out of shots you lose😭')
            break   
     

    

main()

    

