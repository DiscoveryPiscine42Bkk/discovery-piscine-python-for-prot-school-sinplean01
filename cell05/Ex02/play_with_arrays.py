a = [2, 8, 9, 48, 8, 22, -12, 2]
while 2 in a or -12 in a:
    if 2 in a:
        a.remove(2)
    if -12 in a:
        a.remove(-12)
for i in range(len(a)):
    a[i] += 2
print(a)
    