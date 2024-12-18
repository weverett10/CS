#"cat"
import random
import os
import time
os.system('cls')
print("""
              _                          
__      _____| | ___ ___  _ __ ___   ___ 
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \\
 \ V  V /  __/ | (_| (_) | | | | | |  __/
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

""")
time.sleep(2)
possible  = ['rock','paper','scissors']
possible1 = ['rock','paper','scissors','pen','eraser']
score_limit = 5
total_score_player = 0
total_score_computer = 0
player1_total = 0
player2_total = 0
lines = '\n'*45

while True:
    choice = str.lower(input("""
                     _     _                           
__      _____  _   _| | __| |  _   _  ___  _   _       
\ \ /\ / / _ \| | | | |/ _` | | | | |/ _ \| | | |      
 \ V  V / (_) | |_| | | (_| | | |_| | (_) | |_| |      
 _\_/\_/ \___/ \__,_|_|\__,_|  \__, |\___/ \__,_|  
                               |___/
 _ _ _          _   
| (_) | _____  | |_ ___    _ _    ___ ___              
| | | |/ / _ \ | __/ _ \  | | | / __|/ _ \             
| | |   <  __/ | || (_) | | |_| \__ \  __/             
|_|_|_|\_\___|  \__\___/   \__,_|___/\___|  
__  _
| |_| |__   ___   _ __ ___   __ _  __ _(_) ___   ( _ ) 
| __| '_ \ / _ \ | '_ ` _ \ / _` |/ _` | |/ __|  / _ \ 
| |_| | | |  __/ | | | | | | (_| | (_| | | (__  | (_) |
 \__|_| |_|\___| |_| |_| |_|\__,_|\__, |_|\___|  \___/ 
 _           _ _                  |___/                
| |__   __ _| | |   ___  _ __   _ __ | | __ _ _   _    
| '_ \ / _` | | |  / _ \| '__| | '_ \| |/ _` | | | |   
| |_) | (_| | | | | (_) | |    | |_) | | (_| | |_| |   
|_.__/ \__,_|_|_|  \___/|_|    | .__/|_|\__,_|\__, |   
 _ __ ___   ___| | __  _ __   _|_| _ __   ___ |___/    
| '__/ _ \ / __| |/ / | '_ \ / _` | '_ \ / _ \ '__|    
| | | (_) | (__|   <  | |_) | (_| | |_) |  __/ |       
|_|  \___/_\___|_|\_\ | .__/ \__,_| .__/ \___|_|       
 ___  ___(_)___ ___  _|_| _ __ ___|_|                  
/ __|/ __| / __/ __|/ _ \| '__/ __)                  
\__ \ (__| \__ \__ \ (_) | |  \__ \_                   
|___/\___|_|___/___/\___/|_|  |___(_)   
""")).strip()


    if choice == 'rock paper scissors':
        while True:
            score = 0
            bot_score = 0
            thing = str.lower(input("""    
     _                                                   
  __| | ___    _   _  ___  _   _                         
 / _` |/ _ \  | | | |/ _ \| | | |                        
| (_| | (_) | | |_| | (_) | |_| |                        
 \__,_|\___/   \__, |\___/ \__,_|                        
__      ____ _ |___/| |_  | |_ ___                       
\ \ /\ / / _` | '_ \| __| | __/ _ \                      
 \ V  V / (_| | | | | |_  | || (_) |                     
  \_/\_/ \__,_|_| |_|\__|  \__\___/      _           _   
 _ __ | | __ _ _   _    __ _  __ _  __ _(_)_ __  ___| |_ 
| '_ \| |/ _` | | | |  / _` |/ _` |/ _` | | '_ \/ __| __|
| |_) | | (_| | |_| | | (_| | (_| | (_| | | | | \__ \ |_ 
| .__/|_|\__,_|\__, |  \__,_|\__, |\__,_|_|_| |_|___/\__|
|_|_ _  | |__  |___/ _ __ ___|___/ _ _ __     ___  _ __  
 / _` | | '_ \| | | | '_ ` _ \ / _` | '_ \   / _ \| '__| 
| (_| | | | | | |_| | | | | | | (_| | | | | | (_) | |    
 \__,_| |_| |_|\__,_|_| |_| |_|\__,_|_| |_|  \___/|_|    
  __ _    ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __    
 / _` |  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|   
| (_| | | (_| (_) | | | | | | |_) | |_| | ||  __/ |      
 \__,_|  \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|      
  __ _____       _           |_|        _                 
 / /  ____|_ __ | |_ ___ _ __    __ _  | |_ ___           
| ||   _| | '_ \| __/ _ \ '__|  / _` | | __/ _ \          
| ||  |___| | | | ||  __/ |    | (_| | | || (_) |         
| || _____|_| |_|\__\___|_|     \__, |  \__\___/          
 \_\ _ _   _(_) |_\ \              |_|                    
 / _` | | | | | __| |                                    
| (_| | |_| | | |_| |                                    
 \__, |\__,_|_|\__| |                                    
    |_|          /_/     """)).strip()
            if thing == 'computerw' or 'computerl':
                os.system('cls')
            if thing == 'q':
                break
            elif thing == 'computer':
                print('sounds good, lets start')

                while score < score_limit and bot_score < score_limit:
                    question = str.lower(input("""\n                _                                  
 _ __ ___   ___| | __  _ __   __ _ _ __   ___ _ __ 
| '__/ _ \ / __| |/ / | '_ \ / _` | '_ \ / _ \ '__|
| | | (_) | (__|   <  | |_) | (_| | |_) |  __/ |   
|_|  \___/ \___|_|\_\ | .__/ \__,_| .__/ \___|_|   
                      |_|         |_|              
  ___  _ __   ___  ___(_)___ ___  ___  _ __ ___    
 / _ \| '__| / __|/ __| / __/ __|/ _ \| '__/ __|   
| (_) | |    \__ \ (__| \__ \__ \ (_) | |  \__ \   
 \___/|_|    |___/\___|_|___/___/\___/|_|  |___/    """)).strip()
                    computer = random.choice(possible)
                    print("""\n 
                                 _            
  ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __ 
 / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|
| (_| (_) | | | | | | |_) | |_| | ||  __/ |   
 \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|   
  ___| |__   ___  __|_|___                    
 / __| '_ \ / _ \/ __|/ _ \                   
| (__| | | | (_) \__ \  __/                   
 \___|_| |_|\___/|___/\___|                   """,computer)

                    if question == computer:
                        print ('\ntie play again')
                    elif question == 'rock' and computer == 'paper':
                        print ('\nHAHA you lost')
                        score += 1
                    elif question == 'rock' and computer == 'scissors':
                        print('\ncongrats!!! you won')
                        bot_score += 1
                    elif question == 'paper' and computer == 'rock':
                        print ('\ncongrats!!! you won')
                        score += 1
                    elif question == 'paper' and computer == 'scissors':
                        print('\nHAHA you lost')
                        bot_score += 1
                    elif question == 'scissors' and computer == 'paper':
                        print ('\ncongrats!!! you won')
                        score += 1
                    elif question == 'scissors' and computer == 'rock':
                        print('\nHAHA you lost')
                        bot_score += 1            
                    else:
                        print('you cant do that')
                        print('choose one of the options')
                    print ('\nyour current score is',score)
                    print ('\nthe computers score is',bot_score)

                if score > bot_score:
                    print('congratulations player, you win')
                    total_score_player += 1
                else:
                    print('the computer wins')
                    total_score_computer += 1
                print (total_score_player, "-", total_score_computer)

                
                    
            elif thing == 'human':
                player1_score = 0
                player2_score = 0
                while player1_score < score_limit and player2_score < score_limit:
                    player1 = str.lower (input(f'\nplayer 1 choose:')).strip()
                    os.system('cls')
                    player2 = str.lower (input(f'\nplayer 2 choose:')).strip()
                    os.system('cls')

                    if player1 == player2:
                        print('tie go again')
                    elif player1 == 'rock':
                        if player2 == 'paper':
                            print('\ncongratulations player 2 you won')
                            player2_score += 1
                        elif player2 == 'scissors':
                            print('\ncongratulations player 1 you won')
                            player1_score += 1
                    elif player1 == 'paper':
                        if player2 == 'rock':
                            print('\ncongratulations player 1 you won')
                            player1_score += 1
                        elif player2 == 'scissors':
                            print ('\ncongratulations player 2 you won')
                            player2_score += 1
                    elif player1 == 'scissors':
                        if player2 == 'rock':
                            print('\ncongratulations player 2 you won')
                            player2_score += 1
                        elif player2 == 'paper':
                            print('\ncongratulations player 1 you won')
                            player1_score += 1
                    else:
                        print ("you can't do that,choose one of the options")
                    print ('\nplayer 1 chose')
                    print (player1)
                    print('\nplayer 2 chose')
                    print (player2)
                    print ('\nplayer 1, your score is',player1_score)
                    print ('\nplayer 2, your score is',player2_score)


                if player1_score > player2_score:
                    print('congratulations player 1, you win')
                    player1_total += 1
                else:
                    print('congratulations player 2, you win')
                    player2_total += 1
                print (player1_total, "-", player2_total)

                
            elif thing == "computerw":
                print('sounds good, lets start')

                while score < score_limit and bot_score < score_limit:
                    question = str.lower(input("\nrock? paper? or scissors?: ")).strip()
                   
                    if question == 'rock' :
                        print ('\ncomputer chose scissors')
                        score += 1
                    elif question == 'paper':
                        print ('\ncomputer chose rock')
                        score += 1
                    elif question == 'scissors':
                        print ('\ncomputer chose paper')
                        score += 1          
                    else:
                        print('you cant do that')
                        print('choose one of the options')
                    print ('\nyour current score is',score)
                    print ('\nthe computers score is',bot_score)

                if score > bot_score:
                    print('congratulations player, you win')
                    total_score_player += 1
                else:
                    print('the computer wins')
                    total_score_computer += 1
                print (total_score_player, "-", total_score_computer)

            elif thing == "computerl":
                print('sounds good, lets start')

                while score < score_limit and bot_score < score_limit:
                    question = str.lower(input("\nrock? paper? or scissors?: ")).strip()
                   
                    if question == 'rock' :
                        print ('\ncomputer chose paper')
                        bot_score += 1
                    elif question == 'paper':
                        print ('\ncomputer chose scissors')
                        bot_score += 1
                    elif question == 'scissors':
                        print ('\ncomputer chose rock')
                        bot_score += 1          
                    else:
                        print('you cant do that')
                        print('choose one of the options')
                    print ('\nyour current score is',score)
                    print ('\nthe computers score is',bot_score)

                if score > bot_score:
                    print('congratulations player, you win')
                    total_score_player += 1
                else:
                    print('the computer wins')
                    total_score_computer += 1
                print (total_score_player, "-", total_score_computer)


            else:
                print('enter a valid answer')         
    elif choice == 'magic 8 ball':
        question_markings = ['am','was','is','should','could','would','will','when','which','does','what', 'which', 'when', 'where', 'who', 'whom', 'whose', 'why', 'whether','how']

        while True:
            question = input('what is your question: ')
            right_input = question.strip()
            first_word = question.split()[0]
            
            if first_word in question_markings:
                answers = ["""
 _   _  ___  ___ 
| | | |/ _ \/ __|
| |_| |  __/\__ \\
 \__, |\___||___/
 |___/           """, """
 _ __   ___  
| '_ \ / _ \ 
| | | | (_) |
|_| |_|\___/ """, """  _                               
 _ __ ___   __ _ _   _| |__   ___ 
| '_ ` _ \ / _` | | | | '_ \ / _ \\
| | | | | | (_| | |_| | |_) |  __/
|_| |_| |_|\__,_|\__, |_.__/ \___|
                 |___/            """, """   
           _                        _       
  __ _ ___| | __   __ _  __ _  __ _(_)_ __  
 / _` / __| |/ /  / _` |/ _` |/ _` | | '_ \ 
| (_| \__ \   <  | (_| | (_| | (_| | | | | |
 \__,_|___/_|\_\  \__,_|\__, |\__,_|_|_| |_|
| | __ _| |_ ___ _ __   |___/               
| |/ _` | __/ _ \ '__|                      
| | (_| | ||  __/ |                         
|_|\__,_|\__\___|_|                         """]
                response = random.choice (answers)
                print(response)
    else:
        print ('answer the quesiton correctly')

    
        
        


