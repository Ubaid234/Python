# max ()

# Return the largest item in an iterable or the largest of two or more arguments.

# max (strings, dicts with same keys)

max([3,4,1,2]) # 4
max((1,2,3,4)) # 4
max('awesome') # 'w'
max({1:'a', 3:'c', 2:'b'}) # 3

names = ['Arya' , 'Samson' , 'Dora' , 'Tim' , 'Olivander']

print(min(len(name) for name in names))
print(max(names , key = lambda n: len(n)))
print(min(names , key = lambda n: len(n)))
