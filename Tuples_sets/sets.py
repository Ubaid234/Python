# Sets 
# Sets are like formal mathematical sets.
# sets do not have duplicate values
# elements in sets aren't ordered
# you connot access items in a set by index
# sets can be useful if you need to keep track of collection of elements , but don't care about ordering , keys or values and duplicates

# set cannot have duplicates 
s = set({1,2,3,4,4,4,})
print(s)

# creating a new set 

s = set({1,2,4,5, 'a','b',23.4443})
print(s)
 
print(4 in s )
print(8 in s)

# Acessing sets using good old for-loop
for thing in s : 
    print(thing)

# common usecase 
# an example

alphabets = ['a', 'b' , 'c', 'd' , 'r' , 'y' , 'a','b', 'b']
print(set(alphabets));
print(len(set(alphabets)))