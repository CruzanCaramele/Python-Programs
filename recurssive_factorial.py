def recursive_factorial(num):
    #check if base case is reached
    #base case is Zero --> factorial(0) = 1
    if num == 0:
        return 1

    # otherwise do the recurssion
    else:
        return num * recursive_factorial(num-1)
    


print recursive_factorial(5)
