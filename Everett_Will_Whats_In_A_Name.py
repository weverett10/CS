

def reverse(name):
    reverse_name = lower(name[::-1])
    return(reverse_name)
def count_vowels(name):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for character in name:
        if character in vowels:
            count += 1
    return (count)

def count_consanants(name):
    count_con = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for charactors in name:
        if charactors not in vowels:
            count_con += 1
    return (count_con)

def first_name(name):
    parts = name.split(" ")

    name_1 = parts [0]
    

    return(name_1)
    
    

def last_name(name):
    parts = name.split(" ")

    
    
    name_3 = parts [2]

    return(name_3)
    
   


def middle_name(name):    
    parts = name.split(" ")

    
    name_2 = parts [1]
 

    return(name_2)
    
def hyphen(name):
    hyphen = '-'
    if hyphen in name:
        return True
    else:
        return False
    
def upper(name):
    name_out = ' '
    for letter in name:
        if ord(letter) < 122 and ord(letter) > 91:
            num = ord(letter)
            num = num - 32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return(name_out)

def lower(name):
    name_out = ' '
    for letter in name:
        if ord(letter) > 64 and ord(letter) < 91:
            num = ord(letter)
            num = num + 32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return(name_out)

def scramble(name):
    pass

def palindrome(name):
    reversed = reverse(name)
    name = name
    if lower(name) == reversed:
        return True
    else:
        return False
    
def sorted_array(name):
    order = ' '
    real_name = name.replace(' ', '')
    chars = list(real_name)
    sorted_chars = sorted(chars)
    order = order = sorted_chars
    return(order)


def initials(name): 
    final_initials = ' '
    first = first_name(name)
    second = middle_name(name)
    third = last_name(name)

    first_initial = first[0]
    second_initial = second[0]
    third_initial = third[0]

    final_initials = (first_initial + second_initial + third_initial)
    return(upper(final_initials))

def title(name):
    titles = ['Dr.', 'Ms.', 'Mrs.', 'Jr.', 'Sr.', 'III', 'IV', 'PhD', 'MD', 'Professor', 'sir', 'lord', 'lady', 'king']
    if titles in name:
        return True
    else:
        return False
        


def main():
    while True:
        name = input('what is your name: ')
        while True:
            selection = input('''\n What would you like to do with your name?
                            1.)Reverse it ✔️
                            2.)Find the number of vowels ✔️
                            3.)Find the number of consonants ✔️
                            4.)See your first name ✔️
                            5.)See your last name ✔️
                            6.)See your middle name
                            7.)See if your your last name contains a hyphen ✔️
                            8.)Switch all letters to lowercase ✔️
                            9.)Switch all letters to uppercase ✔️
                            10.)scramble the letters 
                            11.)See if your name is a palindrome ✔️
                            12.)Have your name returnes as characters ✔️
                            13.)Get your initials  ✔️
                            14.)See if your name has a title 
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
                print(lower(name))
            elif selection == '9':
                print(upper(name))
            elif selection == '10':
                scramble(name)
            elif selection == '11':
                print(palindrome(name))
            elif selection == '12':
                print(sorted_array(name))
            elif selection == '13':
                print(initials(name))
            elif selection == '14':
                print(title(name))
            else:
                print("that option doesn't exist")
                break


main()

