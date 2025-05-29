import random
import csv
import time
import os

def clear_console(delay): 
    '''
    clears the console
    args:
        delay. waits for a certain amount of time before clearing
    returns:
        nothing
    extraneous:
        nothing
    '''
    time.sleep(delay)
    os.system('cls')
def login(secret_code, tries):
    '''
    sets a limit for the amount of times you can try to enter the code
    args:
        secret_code and tries. what is the code and how many tries you can have
    returns:
        true if you get the code write.
    extraneous:
        if you don't get the code write it says incorect
        if you go over the tries limitr it cleaers the console and ends
    '''
    for i in range(tries):
        code = input('Enter your code: ')

        if code == secret_code:
            print('You are in!')
            clear_console(1)
            return True
        else:
            print(f'Incorrect! You have {tries-i-1} tries left')
    print('Too many attempts! You are banned')
    clear_console(1)
    exit()
def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays: #if is not an array
        raise ValueError("At least one array must be provided.") #raises a value error
    
    num_rows = len(arrays[0]) #

    for arr in arrays: #starts a for loop that alsts the number of times there are arrays
        if len(arr) != num_rows: #if the number of arrays doesnt equeal the numebr of rows
            raise ValueError("All arrays must have the same length.") #raises a value error
    
    with open(filename, 'w', newline='') as csvfile: # when the file is opened start a new line
        csvwriter = csv.writer(csvfile) #starts wriing in the csv file 
        csvwriter.writerow(headers) #writes a header

        for i in range(num_rows): #for the number of roes
            row = [arr[i] for arr in arrays] # starts the first row
            csvwriter.writerow(row) #writes in that row
def add_set(websites, usernames, passwords):
    '''
    adds sets of usernames websites and passwords
    args:
        websites usernames and passswords
    returns:
        the users inputs to the questions into their lists
    extraneous:
        none
    '''
    while True:
        web = input('add the website or press q to quit:  ')

        if web == 'q':
            break
        else:
            user = input('add the username  ')
            pwd = input('add the password (Press "g" to generate)  ')

            if pwd.lower() == "g":
                pwd = generate_password()
                
            websites.append(web)
            usernames.append(user)
            passwords.append(pwd)
        clear_console(1)
def get_index(websites):
    '''
    gets the index of a certain input
    args:
        websites
    returns:
        the index of the website
    extraneous:
        if you dont enter a websiet that is in the code already
    '''
    while True:
        website = input('what website do you want: ')
        if website in websites:
            return websites.index(website)
        else:
            print('that website hasnt been added yet')
def change_entry(websites, usernames, passwords):
    '''
    change an entry 
    args:
        websites usernames and passwords
    returns:
        the index o each thing you want to change and also changes 
    extraneous:
        none
    '''
    index = get_index(websites)
    change_set = input('Which would you like to change? Enter each letter that applies: websites (w), usernames (u), passwords (p)').lower()

    if "w" in change_set:
        websites[index] =  input(f'your old website was {websites[index]}. Enter your new website: ')
    if "u" in change_set:
        usernames[index] =  input(f'your old username was {usernames[index]}. Enter your new username: ')
    if "p" in change_set:
        passwords[index] =  input(f'your old password was {passwords[index]}. Enter your new password: ')
    else:#if "w" not in change_set and "u" not in change_set and "p" not in change_set:
        print('Enter "w", "p" and/or "q"')
def delete_entry(websites, usernames, passwords):
    '''
    deletes a previous entry
    args:
        websites usernames, passwords
    returns:
        deletes parts of the lists
    '''
    index = get_index(websites)
    websites.pop(index)
    usernames.pop(index)
    passwords.pop(index)
def get_password_length():
    '''
    gets the desired password length
    args:
        none
    returns:
        a passwords length
    extraneous:
        if its not an integer
    '''
    while True:
        try:
            length = int(input('How long do you want your password to be'))    

            if length < 4:
                print('Enter a length of at least 4')
                continue
            return length
        except ValueError:
            print ('that is not an integer')

def check_security(pwd, length, display):
    '''
    checks how secure the password is
    args:
        pwd length and display
    returns:
        false or true
    extraneous:
        if the password is not secure
    '''
    if len(pwd) < length or pwd.lower() == pwd or pwd.upper() == pwd or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list('~!@#$%^&*()-+_=?')):
        if display:
            print(f'{pwd} not secure')
        return False
    else:
        if display:
            print(f'{pwd} secure')
        return True

def generate_password():
    '''
    creates a secure password
    args:
        pwd and length
    return:
        a secure password
    extraneous:
        none
    '''
    length = get_password_length()
    
    while True:
        pwd = ''.join(random.sample(list('abcdeABC012~!@#$%^&*()-_+=?'), length)) #ADD ALL LOWERCASE/UPPERCASE LETTERS AND DIGITS INSIDE THE LIST

        if check_security(pwd, length, False):
            print(f'The generated password is {pwd}')
            return pwd

def main():
    '''
    executes the full code
    args:
        all things
    return:
        keeps the passwords usernames and websites
    extraneous:
        if things dont work
    '''
    websites = []
    usernames = []
    passwords = []

    secret_code = input('Enter a code to get into your password keeper (press "g" to generate): ')

    if secret_code.lower() == "g":
        secret_code = generate_password()
        clear_console(3)
    clear_console(2)
    add_set(websites, usernames, passwords)
    login(secret_code, 3)
    clear_console(1)

    while True:
        options = input('''
options:
1: See all of your websites usernames and passwords
2: Access a specific password  
3: Add another entry
4: Change a username or password
5: Delete an entry
6: Export entries to a csv
7: Generate a password
8: Check the security of a password
Choice: ''')

        if options == '1':
            for i in range(len(websites)):
                print(f'\nwebsite:{websites[i]}   username:{usernames[i]},   password:{passwords[i]}')
        elif options == '2':
            i = get_index(websites)
            print(f'website:{websites[i]} username:{usernames[i]}, password:{passwords[i]}')
        elif options == '3':
            add_set(websites, usernames, passwords)
        elif options == '4':
            change_entry(websites, usernames, websites)
        elif options == '5':
            delete_entry(websites, usernames, passwords)
        elif options == '6':
            filename = input('Enter a filename for your csv: ')
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)
            print(f'Data successfully exported to {filename}.csv')
        elif options == '7':
            generate_password()
        elif options == '8':
            pwd = input('Enter password to check: ')
            length = get_password_length()
            check_security(pwd, length, True)
        else:   
            print('invalid')
main()