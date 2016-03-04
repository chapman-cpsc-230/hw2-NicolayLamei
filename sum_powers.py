user_input = input ("Enter an integer greater than 1: ")
b = int(user_input)
n = 0
while n < b:
    b += (b**(n))
    n += 1
    print (n)
