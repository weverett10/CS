import random
'''
Author: Will Everett
Date: 9/30/25
description: practicing functions for CS2: getting different aspects of a name
Bugs: names dont work if you dont input all 3 names. NOT ALL TITLES ARE LISTED ONLY A SPECIFIC AMOUNT.count consonants counts things that aren't letters
challenges: sorted aray, menu, title, Ceaser Cipher
sources: Mr Campbell and Ms. Marciano
 '''
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
            return ' '.join(names)
        else:
            return(names)    
def reverse(name):
    '''
    Description: reverses the name inputed

    Args: name (string) origional input for name

    Returns: the reverse of the inputed name
    '''

    reverse_name = lower(name[::-1])
    return(reverse_name) 
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
    vowels = ['a', 'e', 'i', 'o', 'u']

    for charactors in new:
        if charactors not in vowels:
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
    if names.index(names[-1])< 3 or names.index(names[-1]) < 2:
        return name[0]
    
    else:
        return names[0]
def last_name(name, which):
    '''
    Description: returns the last name form the given name

    Args: name (string) origional input for name

    Returns: last name from given name
    '''
    new = remove_title(name)
    names = new.split(' ')
    if which == 'last' or which == 'both':
        return names[-1]+' '+names[-2]
    else:
        return names[-1]
def middle_name(name,which ): 
    '''
    Description: returns the middle name

    Args: name (string) origional input for name

    Returns: the middle name of the given name
    '''

    new = remove_title(name)
    names = new.split(' ')
    if which == 'last' or which == 'both':
        return ' '.join(names[1:-2])
    elif names.index(names[-1])< 3 or names.index(names[-1]) < 2:
        return 'no middle name present'

    else:
        return ' '.join(names[1:-1])
def hyphen(name):
    '''
    Description: check if there is a hyphen in your name

    Args: name (string) origional input for name

    Returns: returns a boolean(true or false) if it detects a hyphen
    '''
    hyphen = '-'
    if hyphen in name:
        return True
    else:
        return False
def upper(name):
    '''
    Description: changes everything to uppercase

    Args: name (string) origional input for name

    Returns: the name all uppercase
    '''
    name_out = ''

    for letter in name:
        if ord(letter) < 122 and ord(letter) > 91:
            num = ord(letter)
            num -= 32
            letter = chr(num)
            name_out += letter
        else:
            name_out += letter
    return name_out
def lower(name):
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
def scramble(name):
    '''
    Description: scrambles all the letters in your name

    Args: name (string) origional input for name

    Returns: your name scrambled up
    '''
    shuffled = ''
    new_name = name.replace(' ','')
    letters = list(new_name)

    while len(letters) > 0:
        letter = random.choice(letters)
        shuffled += letter
        letters.remove(letter)
    return shuffled 
def palindrome(name):
    '''
    Description: checks if your name is a palindrome

    Args: name (string) origional input for name

    Returns:a boolean (yes or no) if your name is a boolean
    '''
    reversed = reverse(name)
    if lower(name) == reversed:
        return True
    else:
        return False
def sorted_array(name):
    real_name = name.replace(' ', '')
    chars = list(real_name)
    sorted_chars = sorted(chars)
    return ' '.join(sorted_chars)
def check_for_initials(name): 
    initials = ''
    new = remove_title(name)
    names = new.split(' ')

    for n in names:
        initials += n[0]
    return initials
def check_for_title(name):
    titles = ['Dr.', 'Ms.', 'Mrs.', 'Jr.', 'Sr.', 'III', 'IV', 'PhD', 'MD', 'Professor', 'sir', 'lord', 'lady', 'king']
    for title in titles:
        if title in name:
            return True
    return False
def encryption(name):
    pass
    




    
def main():
    while True:
        name = input('what is your full name: ')
        doubles = input('do you have 2 middle names or 2 lasts names, yes or no: ')
        if doubles == 'yes':
            which = input('middle, last, or both? ')
        while True:
                selection = input('''\n What would you like to do with your name?
                                1.)Reverse it ✔️
                                2.)Find the number of vowels ✔️
                                3.)Find the number of consonants ✔️
                                4.)See your first name ✔️
                                5.)See your last name ✔️
                                6.)See your middle name ✔️
                                7.)See if your your last name contains a hyphen ✔️
                                8.)Switch all letters to lowercase ✔️
                                9.)Switch all letters to uppercase ✔️
                                10.)scramble the letters ✔️
                                11.)See if your name is a palindrome ✔️
                                12.)Have your name returnes as characters ✔️
                                13.)Get your initials  ✔️
                                14.)See if your name has a title ✔️
                                15.)Encode your name
                                Choose a number: ''')

                if selection == '1':
                    print(reverse(name))
                elif selection =='2':
                    print(count_vowels(name))
                elif selection == '3':
                    print(count_consanants(name))
                elif selection == '4':
                    print(first_name(name, which))
                elif selection == '5':
                    print(last_name(name, which))
                elif selection == '6':
                    print(middle_name(name,which))
                elif selection == '7':
                    print(hyphen(name))
                elif selection == '8':
                    print(lower(name))
                elif selection == '9':
                    print(upper(name))
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
                    encryption(name)
                else:
                    print("that option doesn't exist")
                    break


main()

