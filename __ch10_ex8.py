import random

def has_duplicates(list):
    list.sort()
    for i in range(0, len(list) - 1):
        if list[i] == list[i + 1]:
            return True
    return False

birthday_list = []
for i in range(0, 23): 
    birthday_list.append(random.randint(1, 365))
 
print has_duplicates(birthday_list)