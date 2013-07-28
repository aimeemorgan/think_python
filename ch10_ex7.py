def is_anagram(word, other):
    return sorted(word) == sorted(other)
    
print is_anagram("shit", "hits")
print is_anagram("aimee", "dan")