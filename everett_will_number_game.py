import random                               #import random
name = input('what is your name?')          #ask player ('What is your name')
print('good luck',name)                     #display ('good luck'name)
correct_guesses = 0                         #set correct guesses to zero
rounds = 0                                  #set rounds to zero

while True:                                 #forever loop
    number = random.randint(1, 10)          #set number to randomly chosen integer between 1-10
    guesses = 5                             #set guesses to 5      

    while guesses > 0:                      #while guesses are greater than 0
        while True:                         #forever loop
            guess = input('The computer has chosen a number between 1 and 10. Guess that number:')   #set guess to input ('The computer has chosen a number between 1 and 10. Guess that number:')
            
            try:                            #attempt to conver guess to an integer
                guess = int(guess)          #attempt to conver guess to an integer

                if guess >= 1 and guess <= 10:  #if the guess is greater than 1 and the guess is less than 10 
                    break                   #end the forever loop
                else:                       #if something else sait
                    print('please enter a number between 1 and 10!')  #display ('please enter a number between 1 and 10!')
            except ValueError:              #handle the case where input is not a valid integer
                print('please enter a number between 1 and 10!')      # #display ('please enter a number between 1 and 10!')
        
        if guess == number:                 #if the guess is the sane as the number
            print('you got it!')            #display ('you got it!')
            correct_guesses += 1            #add 1 to correct answewrs
            break                           #end loop
        elif guess >= number:               #else if guess is greater than the number
            print('your number is too high')#display ('you number is too high')
        else:                               #else
            print('your number is too low') #display ('your number is too low')
        guesses -= 1                        #subtract one form guesses
        if guesses == '0':                  #if there are zero guesses left
            print('you lost this round')    #display ('you lost thisround')
    rounds += 1                             #add 1 to rounds
    while True:                             #forever loop
        play_again = input(f'{name},you have gotten {correct_guesses},correct out of {rounds} rounds, would you like to play again, enter y or no ')  #set play again equal to input name, you have gotten correct correct out of rounds would you like to play again enter y or no
        if play_again == 'no':              #if play again in no
            exit()                          #exit game
        elif play_again == 'y':             #otherwise if play again is y:
            break                           #break
        else:                               #it says somehting else
            print('Invalid Response')       #display 'invalid response'

