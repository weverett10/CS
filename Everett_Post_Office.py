'''
Author: Will Everett
Date: 10/31/25
Description: gets the price for shipping an item based on the distance it is traveling and how big it is.
Bugs: doesnt list the price correctly if it has only one number - wont work if user responds with words
Sources: Ms. Marciano
'''
# 4,4, .009, 02893, 08516 - .23
# 5,7, .013, 07245, 45216 - .43
# 5,6, .2, 45216, 07245 - .45
# 10, 12, .4,15623,89175 - .80
# 10, 12, 30, 21505, 72400 - 4.65

def interpretinfo(info):
    info = info.split(',')
    card_length = float(info[0])
    card_height = float(info[1])
    card_thickness = float(info[2])
    coming_from = int(info[3])
    going_to = int(info[4])
    return card_length, card_height, card_thickness, coming_from, going_to
def get_card_type(card_length, card_height, card_thickness):
    perim = card_length + 2*(card_height + card_thickness)

    if card_length >= 3.5 and card_length <= 4.25 and card_height >=3.5 and card_height<= 6 and card_thickness >= 0.007 and card_thickness <= 0.016:
        return 'post card'
    elif card_length > 4.25 and card_length < 6 and card_height > 6 and card_height < 11.5 and card_thickness >= 0.007 and card_thickness <= 0.015:
        return  'large post card'
    elif card_length >= 3.5 and card_length <= 6.125 and card_height >= 5 and card_height<= 11.5 and card_thickness > 0.016 and card_thickness < 0.25:
        return  'envelope'
    elif card_length > 6.125 and card_length < 24 and card_height >= 11 and card_height<= 18 and card_thickness >= 0.25 and card_thickness <= 0.5:
        return  'large envelope'
    elif card_length >= 24 or card_height > 18 or card_thickness > .5 and perim <= 84:
        return  'package'
    elif card_length >= 24 or card_height > 18 or card_thickness > .5 and perim > 84 and perim <= 130:
        return  'large package'
    else:
        return 'unmailable'
def get_zone(zipcode):
    if zipcode >= 1 and zipcode <= 6999:
        return 1
    elif zipcode  >= 7000 and zipcode <= 19999:
        return 2
    elif zipcode  >= 20000 and zipcode <= 35999:
        return 3
    elif zipcode  >= 36000 and zipcode <= 62999:
        return 4
    elif zipcode  >= 63000 and zipcode <= 84999:
        return 5
    elif zipcode  >= 8500 and zipcode <= 99999:
        return 6
def get_distance(coming_from, going_to):
    comingfromzone = get_zone(coming_from)
    goingtozone = get_zone(going_to)

    if comingfromzone == -1 or goingtozone == -1:
        return 'unmailable'
    return abs(comingfromzone - goingtozone)
def calculate_cost(card_type, distance):
    if card_type == 'unmailable' or distance == 'unmailable':
        return 'Unmailable'
    if card_type == 'post card':
        return .2 + 0.03*distance
    elif card_type == 'large post card':
        return .37 + 0.03*distance
    elif card_type == 'envelope':
        return .37 + .04*distance
    elif card_type == 'large envelope':
        return  .6 + 0.05*distance
    elif card_type == 'package':
        return  2.95 + 0.25*distance
    elif card_type == 'large package':
        return  3.95 + 0.35*distance
def formating(finalprice):
    if finalprice =='unmailable':
        return finalprice
    finalprice = f"{finalprice:.2f}"

    if finalprice[0] == '0':
        finalprice = finalprice[1:]
    return  finalprice
def main():
    info = input('what is the length, height, and thickness of your item, and what zone your mailing from, and to: ')
    card_length, card_height, card_thickness, coming_from, going_to = interpretinfo(info)
    card_type = get_card_type(card_length, card_height, card_thickness)
    distance = get_distance(coming_from, going_to)
    finalprice = (calculate_cost(card_type, distance))
    print(formating(finalprice))
main()