def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first" : "colt" , "second" : "Rusty"}

# display_names(first="Charlie" , second="Sue")
# display_names(names) #nope
display_names(**names)



