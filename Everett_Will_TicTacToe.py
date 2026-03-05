board =   [  
["", "", ""],
["", "", ""],
["", "", ""]]


def playermove(playerup,board):

    while True:
        while True:
            column = input('which column do you want to put it in(1 2 or 3): ')
            if column != '1' and column != '2' and column != '3':
                print("Can't do that!!")
            
                
            row = input ('what row do you want to put it in(1 2 or 3): ')
            if row != '1' and row != '2' and row != '3':
                print (" Can't do that !!!")
            else:
                break
            



        if board[int(row) - 1][int(column) - 1] == '':
            board[int(row) - 1][int(column) - 1] = playerup
            break
        else:
            print("Can't do that!!!")
            break

def win(board):

    if board[0][0] == 'x' and board [0][1] == 'x' and board [0][2] == 'x':
        return ('Congrats X you just Won the game')
    elif board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
        return('Congrats X you just won the game')
    elif board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
        return('Congrats X you just won the game')


    elif board[0][0] == 'x' and board[1][0] == 'x' and board [2][0] == 'x':
        return('Congrats X you just won the game')
    elif board[0][1] == 'x' and board[1][1] == 'x' and board [2][1] == 'x':
        return('Congrats X you just won the game')
    elif board[0][2] == 'x' and board[1][2] == 'x' and board [2][2] == 'x':
        return('Congrats X you just won the game')


    elif board[0][0] == 'x' and board[1][1] == 'x' and board [2][2] == 'x':
        print('Congrats X you just won the game')
    elif board[0][2] == 'x' and board[1][1] == 'x' and board [2][0] == 'x':
        print('Congrats X you just won the game')   



    if board[0][0] == 'o' and board [0][1] == 'o' and board [0][2] == 'o':
        return ('Congrats X you just Won the game')
    elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
        return('Congrats o you just won the game')
    elif board[2][0] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
        return('Congrats o you just won the game')


    elif board[0][0] == 'o' and board[1][0] == 'o' and board [2][0] == 'o':
        return('Congrats o you just won the game')
    elif board[0][1] == 'o' and board[1][1] == 'o' and board [2][1] == 'o':
        return('Congrats o you just won the game')
    elif board[0][2] == 'o' and board[1][2] == 'ox' and board [2][2] == 'o':
        return('Congrats o you just won the game')

        
    elif board[0][0] == 'o' and board[1][1] == 'o' and board [2][2] == 'o':
        return('Congrats o you just won the game')
    elif board[0][2] == 'o' and board[1][1] == 'o' and board [2][0] == 'o':
        return('Congrats o you just won the game')

def tiegame(board):  
    if board[0][0] == '' and board[0][1] == '' and board[0][2] == '' and board[1][0] == '' and board[1][1] == '' and board[1][2] == '' and board[2][0] == '' and board[2][1] == '' and board[2][2] == '':
        pass
    else:
        return("It's a tie!!!")
        

def main():


    playerup = 'x'
    while True:
        playermove(playerup,board)
        if playerup == 'x':
            playerup = 'o'
        else:
            playerup = 'x'
        print(f''' 
{board[0]}
{board[1]}
{board[2]}
''')
        winner = (win(board))
        tie = (tiegame(board))
        if winner == 'Congrats o you just won the game' or winner == 'Congrats x you just won the game':
            print('congrats X you just won')
            question = input('would you like to play again? ')
            if question == 'yes':
                continue
            else:
                print('ok your loss')
                break
        elif tie == "It's a tie!!!":
            question = input('would you like to play again? ')
            if question == 'yes':
                continue
            else:
                print('ok your loss')
                break


main()