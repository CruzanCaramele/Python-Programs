# this procedure, factorial
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(num):

    number = 1
    while num >= 1:
        number = number * num
        num = num - 1
    return number


print factorial(999)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
