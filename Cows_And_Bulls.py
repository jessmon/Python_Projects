import random

print "Welcome to the bulls game... !!!"
input_val = input("Enter the four digit number >> ")
while len(str(input_val)) != 4:
    print "This is not a valid input"
    input_val = input("Enter the four digit number >> ")
try:
    int(input_val)
except ValueError:
    print "This is not a valid number"

a = 0
random_val = ''
while a < 4:
    val = random.choice('0123456789')
    a += 1
    random_val += val

input_val_str = str(input_val)

incr = 0
cow = 0
bull = 0
while incr < 4:
    if input_val_str[incr] == random_val[incr]:
        cow += 1
    elif input_val_str[incr] in random_val:
        bull +=1
    incr = incr + 1
print "Random number is " + random_val
print "You have %r cows and %r bulls" %(cow, bull)
