def check_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n == c ** n):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
def prompt_user():
    a = int(raw_input("Give me a value for a> "))
    b = int(raw_input("Give me a value for b> "))
    c = int(raw_input("Give me a value for c> "))
    n = int(raw_input("Give me a value for n> "))
    
    check_fermat(a, b, c, n)
    
prompt_user()
    