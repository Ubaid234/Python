# Append

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