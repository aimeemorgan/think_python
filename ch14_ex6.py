import urllib

# conn = urllib.urlopen('http://thinkpython.com/secret.html')
# for line in conn:
#	print line.strip()

zip = raw_input("Enter a zip code: ")
zip_url = 'http://www.uszip.com/%s'% zip

conn = urllib.urlopen(zip_url)

for line in conn:
    if '<h2><strong>' in line:
         line2 = line.strip()
         town = line2[12:-51]
    elif 'Total population' in line:  
        line2 = line.strip()
        population = line2[291:-506]

print 'The name of the town for zip code %s is %s.' % (zip, town)
print 'The population of %s is %s.' % (town, population)
    
    

        
        
