# open() and read()
f = open("text.txt")
# print(f.read())

# seek() and readline()
f.seek(0)
# print(f.readline())

# readlines()
f.seek(0)
# print(f.readlines()) # Gives us a list

# closing a file

f.seek(0)
print(f.close())
print(f.closed)