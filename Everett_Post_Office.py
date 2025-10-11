def set(card_type):
    if card_type == 'post card':
        set = 'PCset'
    elif card_type == 'large post card':
        set = 'LPCset'
    return set 
def card_type(card_length, card_height, card_thickness):
    card_type = ''
    if card_length >= 3.5 and card_length <= 4.25 and card_height >=0.007 and card_height<= 0.014:
        card_type += 'post card'
    return card_type
def zones(coming_from,to):
    if coming_from > to:
        zones = coming_from - to 

    else:
        zones = to - coming_from
    return zones




def find_price(coming_from, to, card_length, card_height, card_thickness):
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

    zones = zones(coming_from,to)
    card_type = card_type(card_length, card_height, card_thickness)
    set = set(card_type)

    cost = 0
    cost += set
    cost += zones*card_type

    return cost

def main():
    card_length = input('what is the length of your card')
    card_height = input('what is the heigh of your card')
    card_thickness = input('what is the thickness of your card')
    coming_from = input('what zone are you mailing from')
    to = input('what zone are you mailing to')


main()