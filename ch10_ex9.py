def remove_dups(t):
    s = []
    for i in t:
        if i not in s:
            s.append(i)
    return s

    
t = [1, 2, 2, 2, 3, 4, 5, 6]
print remove_dups(t)

q = [1, 2, 3, 4, 5, 6, 7]
print remove_dups(q)