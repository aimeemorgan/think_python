def is_triangle(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        print "no!"
    else:
        print "omg yes!!!!"
        

def prompt_user():
    a = int(raw_input("What is the length of the first stick?> "))
    b = int(raw_input("What is the length of the second stick?> "))
    c = int(raw_input("What is the length of the third stick?> "))
    
    is_triangle(a, b, c)
    
prompt_user()
    