a = [2, 8, 9, 48, 8, 22, -12, 2]
b = 0
while b < len(a):
    if a[b] < 5:
        a.pop(b)
    else:
        b += 1
i = 0
while i < len(a):
    a[i] += 2
    i += 1 
print(a)