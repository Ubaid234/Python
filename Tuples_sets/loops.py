# We can use a for loop to iterate over a tuple just like a list!

names = ("colt" , "blue" , "rusty" , "lassie")

for name in names : 
    print(name)

i = len(names) -1
while(i >= 0):
    print(names[i])
    i -= 1