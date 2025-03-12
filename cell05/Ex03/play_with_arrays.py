a =  [2, 8, 9, 48, 8, 22, -12, 2]
c = list(set(a))
b = 0
while b < len(c):
    if c[b] < 8:
        c.pop(b)
    else:
        b += 1
i = 0
while i < len(c):
    c[i] += 2
    i += 1 
print(c)