import random


def chorus():
    '''
    function description:
defines the chorus of a song
    args:

    returns:
prints the chorus
    raises:

    '''
    print("We've gotta hold on to what we've got It doesnt make a difference if we make it or not We got each other, and thats a lot for love We'll give it a shot")
def chorus2():
    print("Oh, were half way there Oh-oh, livin on a prayer Take my hand, we'll make it, I swear Oh-oh, livin on a prayer") 
def song():
    print("Tommy used to work on the docks Unions been on strike, he's down on his luck It's tough, so tough")
    print("Gina works the diner all day Working for her man She brings home her pay for love Mmm, for love") 
    chorus()
    chorus2()
    print("Tommys got his six-string in hock Now he's holding in what he used to make it talk So tough, ooh, its tough")
    print("Gina dreams of running away When she cries in the night, Tommy whispers Baby, it's okay, someday")
    chorus()
    chorus2()
    print("Ooh, we gotta hold on, ready or not You live for the fight when thats all that you've got")
    chorus2()
    chorus2()
    chorus2()
def add(x,y):
    '''
    adding two variables
    args:
        x,y
    returns:
        the result of x + y
    '''
    print(x + y)
def print_list(array):
    for element in array:
        print(element)
def in_list(check, array):
    return check in array
def is_integer(parameter):
    try:
        parameter = int(parameter)
        return True
    except ValueError:
        return False 
def get_integers():
    while True:
        num1 = input('give me a number ')
        num2 = input('give me another number ')

        if is_integer(num1) and is_integer(num2):
            return int(num1), int(num2) 
def get_random():
    a, b = get_integers()
    print(random.randint(a, b))

def count_vowel(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for character in string:
        if character in vowels:
            count += 1
    return count

def main():
    song()
    add(2,3)

    array = [1,2,3,4,5,6,7]
    print_list(array)
    print(in_list(8, array))

    print(is_integer("17"))
    get_random()

    print(count_vowel('the best'))
    
main()




    





