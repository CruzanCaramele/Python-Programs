#this procedure tests to see if a word is the same forwards and backwards
#link the word Level, the spelling does not change when done in reverse

def is_palindrome(word):
    if word == "":
        return True
    else:
        
        if word[0] != word[-1]:
            return False
    
        else:
            if word[0] == word[-1]:
                return is_palindrome(word[1:-1])
        
    


print is_palindrome("amanaplanacanalpanama")
