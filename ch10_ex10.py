import time

def build_list_append():
    wordlist = []
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        wordlist.append(word)
    return wordlist
    
def build_list_otherway():
    wordlist = []
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        wordlist = wordlist + [word]
    return wordlist
    

start_time = time.time()
t = build_list_append()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

start_time = time.time()
t = build_list_otherway()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'


        
