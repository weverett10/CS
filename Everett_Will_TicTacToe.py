



def playermove(playerup,board):
    while True:
        while True:
            column = input('which column do you want to put it in? (1 2 or 3): ')
            if column != '1' and column != '2' and column != '3':
                print("Can't do that!!")
            
            row = input ('what row do you want to put it in? (1 2 or 3): ')
            if row != '1' and row != '2' and row != '3':
                print (" Can't do that !!!")
            else:
                break
            



        if board[int(row)][int(column)] == '':
            board[int(row)][int(column)] = playerup
            break
        else:
            print("Can't do that!!!")
            break

def win(board):

    if board[1][1] == 'x' and board [1][2] == 'x' and board [1][3] == 'x':
        return True
    elif board[2][1] == 'x' and board [2][2] == 'x' and board [2][3] == 'x':
        return True
    elif board[3][1] == 'x' and board [3][2] == 'x' and board [3][3] == 'x':
        return True


    elif board[1][1] == 'x' and board[2][1] == 'x' and board [3][1] == 'x':
        return True
    elif board[1][2] == 'x' and board[2][2] == 'x' and board [3][2] == 'x':
        return True
    elif board[1][3] == 'x' and board[2][3] == 'x' and board [3][3] == 'x':
        return True


    elif board[1][1] == 'x' and board[2][2] == 'x' and board [3][3] == 'x':
        return True
    elif board[1][3] == 'x' and board[2][2] == 'x' and board [3][1] == 'x':
        return True   



    if board[1][1] == 'o' and board [1][2] == 'o' and board [1][3] == 'o':
        return True
    elif board[2][1] == 'o' and board [2][2] == 'o' and board [2][3] == 'o':
        return True
    elif board[3][1] == 'o' and board [3][2] == 'o' and board [3][3] == 'o':
        return True


    elif board[1][1] == 'o' and board[2][1] == 'o' and board [3][1] == 'o':
        return True
    elif board[1][2] == 'o' and board[2][2] == 'o' and board [3][2] == 'o':
        return True
    elif board[1][3] == 'o' and board[2][3] == 'o' and board [3][3] == 'o':
        return True


    elif board[1][1] == 'o' and board[2][2] == 'o' and board [3][3] == 'o':
        return True
    elif board[1][3] == 'o' and board[2][2] == 'o' and board [3][1] == 'o':
        return True   

def tiegame(board):  
    if board[1][1] != '' and board[1][2] != '' and board[1][3] != '' and board[2][1] != '' and board[2][2] != '' and board[2][3] != '' and board[3][1] != '' and board[3][2] != '' and board[3][3] != '':
        return True
        

def main():
    board =   [  
    ['~',1  ,2  ,3,],
    [1, "", "", ""],
    [2, "", "", ""],
    [3, "", "", ""]]
    
    playerup = 'x'

    while True:


        
        print(f''' 
{board[0]}
{board[1]}
{board[2]}
{board[3]}
''')
        playermove(playerup,board)

        
        
        if playerup == 'x':
            playerup = 'o'
        else:
            playerup = 'x'

        if win(board) is True:
            print('\n\n congrats you won')
            q = input('do you want to play again? (y/n): ')
            if q.lower() == 'y':   
                board =   [  
    ['~',1  ,2  ,3,],
    [1, "", "", ""],
    [2, "", "", ""],
    [3, "", "", ""]]                     
                continue
            else:

                break

        elif tiegame is True:
            print("\n\nit's a tie")
            q = input('do you want to play again? (y/n): ')            
            if q.lower() == 'y':        
                board =   [  
    ['~',1  ,2  ,3,],
    [1, "", "", ""],
    [2, "", "", ""],
    [3, "", "", ""]]                
                continue
            else:

                break

main()