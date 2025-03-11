a = str(input("What you gotta say? : "))
b = 'STOP'
c = str(input('I got that! Anything else? :'))
while c :
    if c != b:
        c = str(input('I got that! Anything else? :'))
    elif c == b:
        break