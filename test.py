remove_title = 'Henry'
lowercase = 'henry'
final = ''
new1 = remove_title
new = lowercase
choice  = input('do you want to encode or decode your name: ')
shift = 5

if choice == 'encode':
    for ch in new:
        if ch == ' ' or ch == '-':
            final += ch
        else:
            ding = (ord(ch) - ord('a')) 
            dong = ding + shift
            ibity = dong % 26 
            bibity = ibity + ord('a')
            blong = chr(bibity)
            final += blong
    print(final)

elif choice == 'decode':
    for ch in new:
        if ch == ' ' or ch == '-':
            final += ch
        else:
            final += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    print(final)