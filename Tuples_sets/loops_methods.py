# We can use a for loop to iterate over a tuple just like a list!

names = ("colt" , "blue" , "rusty" , "lassie")

for name in names : 
    print(name)

i = len(names) -1
while(i >= 0):
    print(names[i])
    i -= 1

# Methods with tuples 

# Count

x = (1,2,3,4,4,4)
print(x.count(1))
print(x.count(4))

# index()

print(x.index(1))
print(x.index(4)) # only returns the first matching index

