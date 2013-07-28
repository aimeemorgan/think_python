def over_20():
    a = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            a.append(word)     
    return a
        
def has_no_e(word):
    if 'e' not in word:
        return True
    return False
    
print has_no_e('aimee')
print has_no_e('dan')