class Kangaroo(object):
    def __init__(self, pouch_contents=[]):
        self.pouch_contents = pouch_contents
        
    def put_in_pouch(self, a):
        self.pouch_contents.append(a)
        
    def __str__(self):
        return 'Kangaroo %s has pouch contents %s.' % (self, self.pouch_contents)
            
kanga = Kangaroo()
print type(kanga)

roo = Kangaroo()
print type(roo)

kanga.put_in_pouch('wallet')
kanga.put_in_pouch(roo)

print kanga.pouch_contents
print roo
