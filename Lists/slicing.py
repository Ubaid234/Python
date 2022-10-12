# SLICING
# some_list[start:end:step]
# First parameter for slice: start

first_list = [1,2,3,4]
print(first_list[1:])
print(first_list[3:])
print(first_list[20:])

# we can also use negative numbers
# gives the list from that index

first_list = [1,2,3,4]
print(first_list[-1:])
print(first_list[-3:])

# Second parameter for slice: end
# The index to copy up to (exclusive counting).

first_list = [1,2,3,4]
print(first_list[:2])
print(first_list[:4])
print(first_list[1:3])

# With negative numbers, how many items to exclude from the end(i.e indexing by counting backwards)

print(first_list[:-1])
print(first_list[1:-1])

# Third parameter

# step in python is basically the number to count at a time 
# same as step with range

first_list = [1,2,3,4,5,6]
print(first_list[1::2])
print(first_list[::2])

# with negative numbers, reverse the order

print(first_list[1::-1])
print(first_list[:1:-1])
print(first_list[2::-1])


# Tricking with slices 

# Reversing a string / lists
string = 'This is fun!'
print(string[::-1])

# Modifying portions of Lists

numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']
print(numbers)