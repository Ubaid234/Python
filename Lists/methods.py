# Append

from unicodedata import name


first_list = [1,2,3,4]
first_list.append(5)
first_list.append([6,7,8,9])
print(first_list)

# Extent 

second_list = [3,4,9,0]
second_list.extend([1,2,3,8])
print(second_list)

# Insert

third_list = [2,3,4,5]
third_list.insert(0,1) #index and insertion
print(third_list)

# Insert Using negative numbers
third_list.insert(-1 , "Negative")

# To add at the last of the list 
third_list.insert(len(third_list) , "Last")
print(third_list)

# Clear

fourth_list = [3,3,4,4,4,5]
fourth_list.clear()
print(fourth_list)

# Pop

fifth_list = [1,2,3,4,5]
fifth_list.pop() #removes last item by default
fifth_list.pop(2) #remove item at index of 2
print(fifth_list)

# Remove (removes the first item whose value is x)

sixth_list = [1,2,3,22,2,3]
sixth_list.remove(22)
print(sixth_list)

# Index 
# Returns the index of a specified item in the list

seventh_list = [5,5,6,7,5,8,8,9,10]
print(seventh_list.index(5))

# Can specify start and end

seventh_list = [5,5,6,7,5,8,8,9,10]
print(seventh_list.index(5,1)) #-- Gives the index from index of 1
print(seventh_list.index(5,2))

# Start and end Both

seventh_list = [5,5,6,7,5,8,8,9,10]
print(seventh_list.index(8,6,8))
# The above statement gives the index of 8 starting from the idex of 6 to the index of 8.
# Gives error if not in the list

# Count 
# Returns the number of times x appers in the list

eighth_list = [1,2,3,4,3,2,1,10,2]
print(eighth_list.count(2))
print(eighth_list.count(3))
print(eighth_list.count(21)) #Gives 0

# Reverse
# Reverse the elements of the list (in-place)

ninth_list = [9,8,7,5]
ninth_list.reverse()
print(ninth_list)

# Sort
# sort the items in the lists (in-place)
# sorts numbers in acsending order
tenth_list = [6,3,9,2,7]
tenth_list.sort()
print(tenth_list)

# sorts words in alphabatical order
eleventh_list = ['colt' , 'blue', 'sara' , 'aryan' , 'khalid' , 'sahil' , 'jabir']
eleventh_list.sort()
print(eleventh_list)

# sorts capital letters first
eleventh_list = ['colt' , 'blue', 'sara' , 'aryan' , 'khalid' , 'sahil' , 'jabir']
eleventh_list.append('ARYAN')
eleventh_list.sort()
print(eleventh_list)

# JION -->(Actually an string method)
# Used to convert list to strings

words = ['Coding' ' is' ' Fun!']
print(''.join(words))

name = ['Mr', 'Steele']
print('. '.join(name))