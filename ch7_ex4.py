def eval_loop():
    while True:
        string = raw_input("Give me input! >")
        if string == 'done':
            break
        result = eval(string)
        print result
        
    print result
    
eval_loop()