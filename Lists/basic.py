#Basic (creating lists)

demo_list = ["a", 1.23, True, 9]
print(demo_list)

length = len(demo_list)
print(f"Length of the above list is {length} \n")

# variables in lists 

first_task = "Install python"
second_task = "Learn python"
third_task = "Take a break"
print("variables in list ")
tasks = [first_task, second_task , third_task]
print(tasks)

# converting range to lists
print(" \n Convering range into list")
nums = list(range(1, 10))
print(nums)

# Accessing Data in Lists

colors = ["orange" , "Blue" , "White", "Grey"]
print(f"\n{colors[2]}")

# Accessing Data in Lists using negative numbers
print(colors[-3])

# Check if a value is in the list
"Blue" in colors

