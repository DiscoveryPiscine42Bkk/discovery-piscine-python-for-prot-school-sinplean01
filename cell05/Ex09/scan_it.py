import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    word = sys.argv[2]
    words = word.split()

    c = 0
    i = 0  

    while i < len(words):
        if words[i] == keyword:
            c += 1
        i += 1  

    if c > 0:
        print(c)
    else:
        print("none")