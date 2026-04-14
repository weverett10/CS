'''
Author: Will Everett
Date: 4/7/2026
description: game of tic tac toe
Bugs: doesn't tell you who won - doesn't print the final move on a win - 
sources: Mr Campbell and Ms. Marciano and Ms. Sharma
 '''


def playermove(playerup,board):
    '''
    description: decides which players turn it is

    args: player up and board

    returns: which players move it is and where it goes
    '''
    while True:
        while True:
            column = input('which column do you want to put it in? (1 2 or 3): ')
            if column != '1' and column != '2' and column != '3':
                print("Can't do that!!")
                continue
            
            row = input ('what row do you want to put it in? (1 2 or 3): ')
            if row != '1' and row != '2' and row != '3':
                print (" Can't do that !!!")
            else:
                break
            



        if board[int(row)-1][int(column)-1] == ' ':
            board[int(row)-1][int(column)-1] = playerup
            break
        else:
            print("Can't do that!!!")#fix this
            break

def win(board):
    '''
    description: figures out who wins the game

    args: board

    returns: true, telling if the game has been won
    
    '''

    if board[0][0] == 'x' and board [0][1] == 'x' and board [0][2] == 'x':
        return True
    elif board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
        return True
    elif board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
        return True


    elif board[0][0] == 'x' and board[1][0] == 'x' and board [2][0] == 'x':
        return True
    elif board[0][1] == 'x' and board[1][1] == 'x' and board [2][1] == 'x':
        return True
    elif board[0][2] == 'x' and board[1][2] == 'x' and board [2][2] == 'x':
        return True


    elif board[0][0] == 'x' and board[1][1] == 'x' and board [2][2] == 'x':
        return True
    elif board[0][2] == 'x' and board[1][1] == 'x' and board [2][0] == 'x':
        return True   



    if board[0][0] == 'o' and board [0][1] == 'o' and board [0][2] == 'o':
        return True
    elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
        return True
    elif board[2][0] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
        return True


    elif board[0][0] == 'o' and board[1][0] == 'o' and board [2][0] == 'o':
        return True
    elif board[0][1] == 'o' and board[1][1] == 'o' and board [2][1] == 'o':
        return True
    elif board[0][2] == 'o' and board[1][2] == 'o' and board [2][2] == 'o':
        return True

        
    elif board[0][0] == 'o' and board[1][1] == 'o' and board [2][2] == 'o':
        return ('o, you won')
    elif board[0][2] == 'o' and board[1][1] == 'o' and board [2][0] == 'o':
        return True

def tiegame(board):  
    '''
    description: checks if the game was a tie

    args: board

    returns: true, determines if the gaem is a tie
    
    '''

    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        return True
        

def main():

    board =   [  
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]] 
    
    playerup = 'x'

    while True:


        print(f'''  1   2   3
        
1  {board[0][0]} | {board[0][1]} | {board[0][2]}
  -----------
2  {board[1][0]} | {board[1][1]} | {board[1][2]}   
  -----------          
3  {board[2][0]} | {board[2][1]} | {board[2][2]}                   
                      ''')
        playermove(playerup,board)

        
        
        if playerup == 'x':
            playerup = 'o'
        else:
            playerup = 'x'

        if win(board):
            print('\n\n congrats you won')
            q = input('do you want to play again? (y/n): ')
            if q.lower() == 'y':   
                board =   [  
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]     
                continue
            else:

                break

        elif tiegame(board):
            print("\n\nit's a tie")
            q = input('do you want to play again? (y/n): ')            
            if q.lower() == 'y':        
                board =   [  
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]] 
        
                continue
            else:

                break

main()