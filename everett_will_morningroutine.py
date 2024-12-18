import time
while True:                                                                                 #starts a forever loop
    start = input("Start? y/n:")                                                            #stores the users response in variable "start?"
    if start == "y":                                                                        #if the user says y

        print ("\n\nALARM!!!\n\n")                                                          #goes down two lines then displays message "ALARM!!!" then goes down two lines for the next code
        time.sleep (0.5)                                                                    #pauses the code for 0.5 seconds

        while True:                                                                         #starts a forever loop
            snooze = str.lower (input ("\nsnooze the alarm y/n:"))                          #allows for any uppercase to be changed to lowercaes and stores the users reponse in "snooze alarm" after going down a line

            if snooze == "y":                                                               #if the user says y
                print ("\nGo back to sleep for a couple more minutes")                      #goes down one line and displays "go back to sleep for a couple more minutes"
                time.sleep(2)                                                               #code pauses for two seconds
                print ("\nALARM!!!")                                                        #goes down a line and displays "ALARM"
            elif snooze == "n":                                                             #if the user says n
                print ("\nGet out of bed")                                                  #goes down a line and displays "get out of bed"
                time.sleep (0.3)                                                            #pauses code for 0.3 seconds
                print ("get dressed for school")                                            #displays "get dressed for school"
                break                                                                       #leaves the forever loop
            else:                                                                           #if user puts in a response that is not y or n
                print("\n\nINVALID RESPONSE!")                                              #goes down two lines and displays "INVAID RESPONSE!"

        while True:                                                                         #starts forever loop
            homework = str.lower (input ("\n\nDo i have any Homework left? y/n:"))          #allows for any uppercase to be changed to lowercaes and stores the users reponse in "Do i have any Homework left? after going down two lines

            if  homework == "y":                                                            #if the user says y
                print ("\ndo homework")                                                     #goes down a line and displays "do homework"
            elif homework == "n":                                                           #if the user says n 
                print ("\nplay on your phone")                                              #goes down a line and displays "play on your phone"
                break                                                                       #leaves the forever loop
            else:                                                                           #if the user puts in a response that is not y or n
                print ("\n\nINVALID RESPONSE!")                                             #goes down two lines and displays "INVALID RESPONSE!"

        hungry = str.lower (input ("\n\nAm I hungry? y/n:"))                                #allows for any uppercase to be changed to lowercaes and stores the users reponse in "Am I hungry?" after going down two lines

        if hungry == "y":                                                                   #if the user says y
            print ("\ngo get food")                                                         #goes down a line and displays "go get food"
        elif hungry == "n":                                                                 #if the user inputs "n"
            print ("\nkeep playing on your phone")                                          #goes down a line and displays "keep playing on your phone"
        else:                                                                               #if the user puts in a response that is not y or n
            print ("\n\nINVALID RESPONSE!")                                                 #goes down to lines and displays "INVAID RESPONSE!"

            
        while True:                                                                         #starts a forever loop
            leave = str.lower (input ("\n\nis it time to go y/n:"))                           #allows for any uppercase to be changed to lowercaes and stores the users reponse in "is it time to go" after going down a line

            if leave == "y":                                                                #if the user says y
                print("\nget in the car")                                                   #goes down a line and displays "get in the car"
                break                                                                       #leaves the forever loop
            elif leave == "n":                                                              #if the user says n
                time.sleep(0.5)                                                             #pauses code for 0.5 seconds
                print ("\nstay on the phone")                                               #goes down a line and displays "stay on the phone
            else:                                                                           #if the user puts in a response that is not y or n
                print ("\n\nINVALID RESPONSE!")                                             #goes down two lines and displays "INVALID RESPONSE!"

            
        while True:                                                                         #starts a forever loop
            At_school = str.lower (input ("\n\nAre we at school yet? y/n:"))                #allows for any uppercase to be changed to lowercaes and stores the users reponse in "are we at school yet? after going down two lines

            if At_school == "y":                                                            #if the user says y
                print ("\nget out of the car")                                              #goes down a line and display "get out of the car"
                time.sleep (0.3)                                                            #pauses the code for 0.3 seconds
                print ("walk into school")                                                  #displays "walk into school"
                break                                                                       #leaves the forever loop
            elif At_school == "n":                                                          #if the user says n
                print ("\nstay in the car")                                                 #goes down a line and displays "stay in car"
                time.sleep(0.5)                                                             #pauses the code for 0.5 seconds
            else:                                                                           #if the user puts in a response that is not y or n
                print ("\n\nINVALID RESPONSE!")                                             #goes down two lines and displays "INVALID RESPONSE"



        while True:                                                                         #starts a while true loop
            hungry = str.lower (input ("\n\nam I hungry yet y/n:"))                         #allows for any uppercase to be changed to lowercaes and stores the users reponse in "am i hungry yet" after going down two lines            

            if hungry == "y":                                                               #if the user says y
                print ("\ngo get breakfast")                                                # goes down a line then displays go get breakfast
                break                                                                       #leaves the forever loop
            elif hungry == "n":                                                             #if the user says n
                time.sleep (0.5)                                                            #pauses the code for 0.5 seconds
                print ("\nwait for food")                                                   #goes down a line then displays "wait for food"
            else:                                                                           #if the user puts in a response that is not y or n
                print ("\n\nINVALID RESPONSE!")                                             #goes down two lines then prints "INVALID RESPONSE!"



        homework = str.lower (input ("\n\ndo i have any more homework to do y/n:"))         #allows for any uppercase to be changed to lowercaes and stores the users reponse in "do i have any more homework to do" after going down two lines

        if  homework == "y":                                                                #if the user says y
            print ("\nfinish homework")                                                     # goes down a line and prints "finish homework"
        elif homework == "n":                                                               #if the user says n
            print ("\nhangout")                                                             #goes down a line and displays "hangout"
        else:                                                                               #ifthe user puts in a response that is not y or n
            print ("\n\nINVALID RESPONSE!")                                                 #goes down two lines and displays


        while True:                                                                         #starts a forever loop
            school_start = str.lower (input ("\n\nis it time to go to advisory y/n:"))      #allows for any uppercase to be changed to lowercaes and stores the users reponse in "is it time to go to advisory" after going down to lines

            if school_start == "y":                                                         #if the user says y
                print ("\ngo to advisory")                                                  #goes down a line and prints go to advisory
                time.sleep (0.3)                                                            #pauses the code for 0.3 seconds
                print ("turn your phone in")                                                #displays turn your phone in
                break                                                                       #leaves the forever loop
            elif school_start == "n":                                                       #if the user says n
                time.slep (0.5)                                                             #pauses the code for 0.5 seconds
                print ("\nwait")
            else:
                print ("\n\nINVALID RESPONSE!")

        time.sleep(3.5)

        print ("\n\n\nschool day is over")
        print ("go get your phone from advisory")


        time = str.lower (input ("\nis it before 3:10 y/n:"))

        if time == "y":
            print ("\ngo to the locker room")
            time.sleep (0.3)
            print ("put your bag away")
            time.sleep (0.3)
            print ("get changed")
            time.sleep (0.3)
            print ("wait for meeting to start")
        elif  time  == "n":
            print ("\ngo get a snack")
            time.sleep (0.3)
            print ("wait until the meeting starts")
        else:
            print ("\n\nINVALID RESPONSE!")


        while True:
            practice = str.lower (input ("\nis practice over y/n:"))

            if practice == "y":
                print ("\ngo to the locekr room")
                time.sleep (0.3)
                print ("take off pads")
                time.sleep (0.3)
                print ("get bag")
                time.sleep (0.3)
                print ("wait to get picked up")
                break
            elif practice == "n":
                print ("\nwait for practice to end")
                time.sleep(0.5)
            else:
                print ("\n\nINVALID RESPONSE!")


        while True:
            ride_here = str.lower (input ("\nis it time to get picked up y/n:"))

            if ride_here == "y":
                print ("\nget in car")
                time.sleep (0.3)
                print ("wait to get home")
                break
            elif ride_here == "n":
                time.sleep(0.5)
                print ("\nwait")
            else:
                print ("\n\nINVALID RESPONSE!")


        while True:
            at_home = str.lower (input ("\nare we at home yet y/n:"))

            if at_home == "y":
                print ("\nget out of the car")
                time.sleep (0.3)
                print ("close garage")
                time.sleep (0.3)
                print ("walk into the house")
                break
            elif at_home == "n":
                time.sleep(0.5)
                print ("\nwait a bit longer")
            else:
                print ("\n\nNVALID RESPONSE!")

        homework_amount = str.lower (input ("\ndo you have a lot of homework y/n:"))

        if homework_amount == "y":
            print ("\ngo do homework ")
        elif homework_amount == "n":
            time.sleep (0.5)
            print ("\nrelax for a bit then start homework")
        else:
            print ("\n\nINVALID RESPONSE!")


        while True:
            homework = str.lower (input ("\nare you done with homework for the night y/n:"))

            if homework == "y":
                print ("\nwalk downstairs")
                print ("eat dinner")
                break
            elif homework == "n":
                time.sleep (0.5)
                print ("\nkeep working")
            else:
                print ("\n\nINVALID RESPONSE!")

        while True:
            dinner = str.lower (input ("\nare you done with dinner yet y/n:"))

            if dinner == "y":
                print ("\nchill out")
                break
            elif dinner == "n":
                time.sleep (0.5)
                print ("\nkeep eating")
            else:
                print ("\n\nINVALID RESPONSE!")


        TV = str.lower (input ("\ndo you want to watch TV y/n:"))

        if TV == "y":
            print ("\nturn on Tv")
            print ("put something on")
        elif TV == "n":
            print ("\ngo on your phone")
        else:
            print ("\n\nINVALID RESPONSE!")

        while True:
            tired = str.lower (input ("\nare you tired y/n:"))

            if tired == "y":
                print ("\ngo upstairs")
                time.sleep(0.3)
                print ("get changed")
                time.sleep (0.3)
                print ("brush teeth")
                break
            elif tired == "n":
                time.sleep (0.5)
                print ("\nkeep doing what you're doing")
            else:
                print ("\n\nINVALID RESPONSE!")
    elif start == "n":
        print ("wrong answer")
        print ("try again")
    else:
        print("\n\nINVALID RESPONSE!")
                

        



        








        
        
        
            

            




            


            
                

        



