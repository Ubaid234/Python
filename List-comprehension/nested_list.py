# Nested lists 

# Lists can contain any kind of element, even other lists 

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

# Accessing nested lists
print(nested_list[0][1])
print(nested_list[1][2])

# Using negative numbers 
print(nested_list[-1][2])

# Printing Values in Nested Lists
# With loops

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for l in nested_list:
    for val in l:
        print(val)

coords = [[10.423, 9.132], [37.212, -14.092], [21.234, 32.232]]

for loc in coords:
    for coord in loc:
        print(coord)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print([[print(val) for val in l] for l in nested_list])

board = [[num for num in range(1,4)] for val in range (1,4)]
print(board)
board = [["X" if num % 2 !=0 else "O" for num in range(1,4)] for val in range(1,4)]
print(board)