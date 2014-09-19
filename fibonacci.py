def fibonacci(num):
    if num == 0:
        return 0 
    if num == 1:
        return 1
    
    else:
        if num > 1:
            return (fibonacci(num -1 )) + (fibonacci(num -2))




def faster_fibonacci(num):

    current = 0
    after = 1

    for i in range(0, num):
        current, after = after, current + after
    return current
        
        
    
    
#print fibonacci(0)
mass_of_earth = 5.9722 * 10**24
mass_of_rabbit = 2
num = 1
#print faster_fibonacci(60)
while faster_fibonacci(num) * mass_of_rabbit < mass_of_earth:
    num += 1
print num, faster_fibonacci(num)
    

