def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
    if first(word) != last(word):
        return False
    elif first(word) == last(word) and len(middle(word)) > 1:
        is_palindrome(middle(word))
    return True

print is_palindrome("redivider")