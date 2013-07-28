def has_no_e(word):
    if 'e' not in word:
        return True
    return False

def avoids(word, string):
    for c in word:
        if c in string:
            return False
    return True    
    
def avoids_list():
    a = []
    fin = open('words.txt')
    forbidden = raw_input("Enter some forbidden letters: >")
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden) == True:
            a.append(word)     
    return a
    
def uses_only(word, string):
    for c in word:
        if c not in string:
            return False
    return True   
    
def uses_all(word, string):   
    for c in string:
        if c not in word:
            return False
    return True

def uses_all_list(letters):
    a = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_all(word, letters) == True:
            a.append(word)     
    return a

def is_abecedarian(word):
    if len(word) == 1:
        return True
    else:
        for i in range(0, len(word) - 1):
            if word[i] > word[i + 1]:
                return False
        return True
        
def is_abecedarian_list():
    a = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word) == True:
            a.append(word)     
    return a

    
print is_abecedarian_list()

# print uses_all_list('aeiou')
# print uses_only('aimee', 'aies')   
# print len(avoids_list())


