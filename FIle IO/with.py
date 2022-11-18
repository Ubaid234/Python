# Option 1 

# file = open("text.txt")
# print(file.read())
# file.close()

# print(file.closed)

# Option 2 

with open("text.txt") as f : 
    print(f.read())

print(f.closed)




