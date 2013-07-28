def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0 and is_power((a / b), b):
        return True
    return False
    
print is_power(32, 2)
