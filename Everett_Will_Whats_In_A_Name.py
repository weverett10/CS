import random
'''
Author: Will Everett
Date: 9/30/25
description: practicing functions for CS2: getting different aspects of a name
Bugs: Not all titles listed
sources: Mr Campbell and Ms. Marciano
 '''
def uppercase(name):
    '''
    Description: changes everything to uppercase

    Args: name (string) origional input for name

    Returns: the name all uppercase
    '''
    name_out = ''

    for letter in name:
        if ord(letter) < 122 and ord(letter) > 96:
            num = ord(letter)
            num -= 32
            letter = chr(num)
            name_out += letter
        else:
            name_out += letter
    return name_out
def lowercase(name):
    '''
    Description: turns the name all lowercase

    Args: name (string) origional input for name

    Returns: the name all lowecase
    '''
    name_out = ''

    for letter in name:
        if ord(letter) > 64 and ord(letter) < 91:
            num = ord(letter)
            num += 32
            letter = chr(num)
            name_out += letter
        else:
            name_out += letter
    return name_out
def remove_title(name):
    '''
    Description: removes the title in a name

    Args: name (string)origional input for name

    Returns: the name without a title in it
    '''
    titles = ['Dr.', 'Ms.', 'Mrs.', 'Jr.', 'Sr.', 'III', 'IV', 'PhD', 'MD', 'Professor', 'sir', 'lord', 'lady', 'king']
    names = name.split(' ')

    for title in titles:
        if title in names:
            names.remove(title)
    listed =  ' '.join(names)  
    return listed.strip()  
def reverse(name):
    '''
    Description: reverses the name inputed

    Args: name (string) origional input for name

    Returns: the reverse of the inputed name
    '''
    return lowercase(name[::-1])
def count_vowels(name):
    '''
    Description: conuts the amount of vowels in the name

    Args: name (string) origional input for name

    Returns: a number that is the aomunt of vowels in the name
    '''
    new = remove_title(name)
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for character in new:
        if character in vowels:
            count += 1
    return count
def count_consanants(name):
    '''
    Description: counts the amount of consonants in the name 

    Args: name (string) origional input for name

    Returns: an number that is the amount of consonants in the name
    '''
    new = remove_title(name)
    count_con = 0
    consenants = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B', 'C', 'D', 'F', 'G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

    for charactors in new:
        if charactors in consenants:
            count_con += 1
    return count_con
def first_name(name):
    '''
    Description: returns the first name that was given

    Args: name (string) origional input for name

    Returns: first name of the person
    '''
    new = remove_title(name)
    names = new.split(' ')
    return names[0]
def last_name(name):
    '''
    Description: returns the last name form the given name

    Args: name (string) origional input for name

    Returns: last name from given name
    '''
    new = remove_title(name)
    names = new.split(' ')
    return names[-1]
def middle_name(name): 
    '''
    Description: returns the middle name

    Args: name (string) origional input for name

    Returns: the middle name of the given name
    '''
    new = remove_title(name)
    names = new.split(' ')
    return ' '.join(names[1:-1])
def hyphen(name):
    '''
    Description: check if there is a hyphen in your name

    Args: name (string) origional input for name

    Returns: returns a boolean(true or false) if it detects a hyphen
    '''
    return '-' in last_name(name)
def scramble(name):
    '''
    Description: scrambles all the letters in your name

    Args: name (string) origional input for name

    Returns: your name scrambled up
    '''
    shuffled = ''
    new_name = name.replace(' ','')
    letters = list(new_name)
    if '-' in letters:
        letters.remove('-')

    while len(letters) > 0:
        letter = random.choice(letters)
        shuffled += letter
        letters.remove(letter)
    return lowercase(shuffled) 
def palindrome(name):
    '''
    Description: checks if your name is a palindrome

    Args: name (string) origional input for name

    Returns:a boolean (yes or no) if your name is a boolean
    '''
    return lowercase(name) == reverse(lowercase(name))
def sorted_array(name):
    '''
    Description: turns you rname into an alphabetical list of charactors

    Args: name (string) origional input for name

    Returns:your name as a list of charactors alphabetical
    '''
    real_name = name.replace(' ', '')
    real_name = name.replace('-','')
    chars = list(real_name)
    sorted_chars = sorted(chars)
    final = ' '.join(sorted_chars)
    return lowercase(final)
def check_for_initials(name): 
    initials = ''
    new = remove_title(name)
    names = new.split(' ')

    for n in names:
        initials += n[0]
    return uppercase(initials)
def check_for_title(name):
    '''
    Description: checks if your name has a title

    Args: name (string) origional input for name

    Returns: boolean (yes or no) if your name has a title in it
    '''
    titles = ['Dr.', 'Ms.', 'Mrs.', 'Jr.', 'Sr.', 'III', 'IV', 'PhD', 'MD', 'Professor', 'Sir', 'Lord', 'Lady', 'king']
    for title in titles:
        if title in name:
            return True
    return False
def encryption(name):
    '''
    description: encodes or decoddes your name
    Args: name (string) origional input for name
    Returns: your name as eithe encoded or a decoded version of your name'''
    final = ''
    new1 = remove_title(name)
    new = lowercase(new1)
    choice  = input('do you want to encode or decode your name: ')
    if choice == 'encode':
        key = input('what do you want the key to be')
        for ch in new:
            if ch == ' ' or ch == '-':
                final += ch
            else:       
                final += chr((ord(ch) + key - 97) % 26 + 97)


        return final
    elif choice == 'decode':
        key = input('what was the key')
        for ch in new:
            if ch == ' ' or ch == '-':
                final += ch
            else:
                final += chr((ord(ch) - ord('a') - key ) % 26 + ord('a'))
        return final
    
    
    




    
def main():
    name = input('what is your full name: ')
    while True:
        while True:
                selection = input('''\n What would you like to do with your name?
                                1.)Reverse it 
                                2.)Find the number of vowels 
                                3.)Find the number of consonants 
                                4.)See your first name 
                                5.)See your last name 
                                6.)See your middle name 
                                7.)See if your your last name contains a hyphen 
                                8.)Switch all letters to lowercase 
                                9.)Switch all letters to uppercase
                                10.)scramble the letters 
                                11.)See if your name is a palindrome 
                                12.)Have your name returned as characters 
                                13.)Get your initials  
                                14.)See if your name has a title 
                                15.)Encode your name
                                16.)Change name
                                Choose a number: ''')

                if selection == '1':
                    print(reverse(name))
                elif selection =='2':
                    print(count_vowels(name))
                elif selection == '3':
                    print(count_consanants(name))
                elif selection == '4':
                    print(first_name(name))
                elif selection == '5':
                    print(last_name(name))
                elif selection == '6':
                    print(middle_name(name))
                elif selection == '7':
                    print(hyphen(name))
                elif selection == '8':
                    print(lowercase(name))
                elif selection == '9':
                    print(uppercase(name))
                elif selection == '10':
                    print(scramble(name))
                elif selection == '11':
                    print(palindrome(name))
                elif selection == '12':
                    print(sorted_array(name))
                elif selection == '13':
                    print(check_for_initials(name))
                elif selection == '14':
                    print(check_for_title(name))
                elif selection == '15':
                    print(encryption(name))
                elif selection == '16':
                    name = input('what is your full name: ')
                    break
                else:
                    print("that option doesn't exist")
                    break


main()