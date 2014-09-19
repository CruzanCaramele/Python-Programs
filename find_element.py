# this procedure, find_element,
# takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(lst, any_data):
    ans = 0
    for elements in lst:
        if elements == any_data:
            return ans
        ans +=1
    return -1
        





#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1




# this procedure, find_element2,
# uses index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element2(lst, any_value):
    
    if any_value in lst:
        return lst.index(any_value)
    else:
        return -1
    




#print find_element2([1,2,3],3)
#>>> 2

#print find_element2(['alpha','beta'],'gamma')
#>>> -1


# this  procedure, union,
# takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(lst_a, lst_b):
    for num in lst_b:
        if num not in lst_a:
            a = lst_a.append(num)
    




# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]

































































