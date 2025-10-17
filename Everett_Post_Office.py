#condense!!
#change input to a list like 4,4,4,0001,00111

def interpretinfo(info):
    infoo = info.split(',')
    card_length = infoo[0]
    card_height = infoo[1]
    card_thickness = infoo[2]
    coming_from = infoo[3]
    going_to = infoo[4]
    return card_length, card_height, card_thickness, coming_from, going_to

print(interpretinfo('4,4,4,00000908,0000000090'))

def card_type(card_length, card_height, card_thickness):
    pre_perim = card_length + card_height + card_thickness
    perim = pre_perim*2

    card_type = ''
    if card_length >= 3.5 and card_length <= 4.25 and card_height >=3.5 and card_height<= 6 and card_thickness >= 0.007 and card_thickness <= 0.016:
        card_type += 'post card'
        return 'PCset'
    elif card_length >= 4.25 and card_length <= 6 and card_height >= 6 and card_height<= 11.5 and card_thickness >= 0.007 and card_thickness <= 0.015:
        card_type += 'large post card'
        return 'LPCset'
    elif card_length >= 3.5 and card_length <= 6.125 and card_height >= 5 and card_height<= 11.5 and card_thickness >= 0.016 and card_thickness <= 0.25:
        card_type += 'envelope'
        card_set = 'Envset'
    elif card_length >= 6.125 and card_length <= 24 and card_height >= 11 and card_height<= 18 and card_thickness >= 0.25 and card_thickness <= 0.5:
        card_type += 'large envelope'
        card_set = 'LEnvset'
    elif card_length >= 25 and card_height >= 11 and card_thickness >= 18 and perim <= 84:
        card_type += 'package'
        card_set = 'Packset'
    elif card_length >= 25 and card_height >= 11 and card_thickness >= 18 and perim >= 85 and perim <= 130:
        card_type += 'large package'
        card_set = 'LPackset'
    else:
        card_type += 'unmailable'
    return card_type, card_set
def zones(zipcode):
    if 1 <= zipcode <= 6999:
        return 1




def find_price(coming_from, going_to, card_length, card_height, card_thickness):
    post_card = 0.03
    PCset = 0.20
    large_post_card = 0.03
    LPCset = 0.37
    envelope = 0.04
    Envset = 0.60
    large_envelop = 0.05
    LEnvset = 0.60
    package = 0.25
    Packset = 2.95
    large_package = 0.35
    LPackset = 3.95

    zones = zones(coming_from,going_to)
    card_type = card_type(card_length, card_height, card_thickness)
    set = set(card_type)

    cost = 0
    cost += set
    cost += zones*card_type

    return cost

def main():
    info = 'what is the length, height, and thickness f your car, and what zone your mailing from, and to' 

    card_length = input('what is the length of your card')
    card_height = input('what is the heigh of your card')
    card_thickness = input('what is the thickness of your card')
    coming_from = input('what zone are you mailing from')
    to = input('what zone are you mailing to')

    mailable = card_type(card_length, card_height, card_thickness)

    if mailable == 'unmailable':
        print('your productis unmailable')
    else:
        print(f'the final price to mail your is', find_price(coming_from, to, card_length, card_height, card_thickness))


main()