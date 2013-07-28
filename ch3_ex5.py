def do_twice(f, a):
    f(a)
    f(a)
    
def print_twice(b):
    print b
    print b
    
    
def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)
 
do_four(print_twice, 'Aimee')