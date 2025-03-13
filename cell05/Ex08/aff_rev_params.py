import sys
a = sys.argv[1:]
b = len(a)
re = a[::-1]
if b <= 2:
    print('none')
else:
    print (re)