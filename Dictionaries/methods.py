# Methods in Dictionaries 

# Clear -- clears the dictionaries
d = dict(a=1,b=2,c=3);
print(d.clear());


# Copy -- copies the dictionaries but memory allocation is different

d = dict(a=1,b=2,c=3);
clone = d.copy()
print(clone)

# fromkeys -- creates key-value pairs from comma seperated values

print({}.fromkeys("a","b"))
print({}.fromkeys(["email" , "name", "Bio" , "gender"] ,'unknown'))
print({}.fromkeys("phone", "unknown"))
print({range(1,10), 'unknown'})


# Get -- retrieves a key in an object and return None instead of a keyError if the key does not exist:

d = dict(a=1, b=2, c=3)
print(d['a'])
print(d.get('a'))
# print(d['no key']) Gives error
print(d.get('no key')) # None

# pop  

d = dict(a=1, b=2, c=3)
# d.pop() -- gives error 
print(d.pop('a'))
# d.pop('e') -- gives error

# popitem --removes a random key in dictionary

d = dict(a=1, b=2, c=3)
print(d.popitem())
# d.popitem("a") -- gives error

# Update -- update keys and values in a dictionary with another set of key value pairs

first = dict(a=1 , b = 2 , c= 3 , d= 4 , e = 5)
second = {}
second.update(first)
print(second)
second['a'] = 23
print(second)
second.update(first)
print(second)

