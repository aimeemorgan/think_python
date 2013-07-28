def has_duplicates(a):
    b = {}
    for i in a:
        if i in b:
            return True
        else:
            b[i] = 1
    
    return False
    
    
print has_duplicates([1, 2, 2, 3])
print has_duplicates([1, 2, 3, 4])