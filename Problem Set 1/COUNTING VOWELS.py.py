x = list(s)
count  = 0
for i in x:
    if i in ['a','e','i','o','u']:
        count = count + 1
print 'Number of vowels: %d'%count  