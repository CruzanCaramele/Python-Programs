# the procedure below, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.



def abbaize(string_one, string_two):
    abbaized_string = string_one + string_two + string_two + string_one
    return abbaized_string


print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'
