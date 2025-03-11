a = int(input('Enter a number less than 25: '))
b = a+5
if a <= 25:
    for i in range(a,b):
        print("Inside the loop, my variable is ",i+1)
else:
    print("Error")