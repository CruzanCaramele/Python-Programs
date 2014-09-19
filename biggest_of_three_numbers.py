# this procedure, biggest, takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(num1, num2, num3):

    if num2 < num1:
        if num3 < num1:
            return num1


    if num1 < num2:
        if num3 < num2:
            return num2

    if num1 < num3:
        if num2 < num3:
            return num3

    if num1 == num2 or num1 == num3:
        return num1

    if num2 == num3:
        return num3
    
# this procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(input):
    
    numbers = 0
    while numbers < input:
        numbers += 1
        print numbers
    
                  
   



print_numbers(3)
#>>> 1
#>>> 2
#>>> 3



print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
