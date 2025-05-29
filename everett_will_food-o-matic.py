import random


foods = ['pork', 'chicken tender', 'spaghetti', 'cheesburger', 'pizza', 'penne pasta', 'tacos', 'steak', 'hot dogs']        #creates a list of foods
prices = [23, 12, 14, 18, 22, 21, 25, 30, 24] #REMOVE QUOTES AND $ (NUMBERS ONLY)     creates a list of prices
flairs =['with mushrrom dressing', 'with ketchup', 'with meatballs', 'with bacon', 'pepporoni', 'with paramsean', 'wity chips and guac', 'with fries', 'with ketchup']      #creates a list of flairs
drinks = ['water', 'apple juice', 'orange juice', 'shirley temple', 'milk']  #creates a list of drinks
drink_prices = [2, 4, 4, 8, 5]      #creates another list of prices

while True: #starts a forever loop
    game = input('what game do you want to play:').lower()      #asks the user a question and stores there response lower case in game

    if game == 'food-o-matic':  #if user says food-o-matic
        print('ok')  #display the word ok
  
        try: #trys to do something
            num_of_items = int(input("How many items would you like? ")) #ask user how many items would you like and store it as an integer in num_of_items
        except ValueError:     #if it cant turn the response into an integer
            print('Please enter a number')  #display please enter a number
            continue    #re aks the question

        if num_of_items >= 14:  #if the users respons is more than 14
            print('thats too many try again')   #displays thats to many try again
            continue    #re asks the question

        total = 0   #defines total as 0

        for i in range(num_of_items):   #for the amount of items the user sys
            food = random.choice(foods) #randomly generate from foods
            flair = random.choice(flairs) #randomly generate from flairs
            drink = random.choice(drinks)  #randomly geerate from drink
            price = prices[foods.index(food)]#get the index of food in foods (how to get the index of an element in a list in python)
            drink_price = drink_prices[drinks.index(drink)] #getrs the index from drink

            print(f'dish: {food} {flair}, drink: {drink}, price: ${drink_price + price}')   #displays the dish the flair the frink an how much the total cost is 
            total += price + drink_price    #calculates the total price
        
        print('your price for food and drink is $', total)  #dislays your price for food and drink is and then displays the total price
    
    elif game == 'number game':     #if the user says number game
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
                    break                          #exit game
                elif play_again == 'y':             #otherwise if play again is y:
                    break                           #break
                else:                               #it says somehting else
                    print('Invalid Response')       #display 'invalid response'
            if play_again == 'no':
                break
    else:
        print('Invalid')
