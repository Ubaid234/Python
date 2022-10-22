# What is a Function

# A process for executing a task 
# It can accept input and return an output
# Useful for executing similar procedures over and over

# Why Use Functions

# Stay DRY - Don't Repeat Yourself!
# Clean up and prevent code duplication

#FUNCTION STRUCTURE
# def name_of_funtion():
#     block of runnable code 

def say_hi(): 
    print('Hi')

say_hi()
say_hi()
say_hi()

# returning a function

def say_hi():
    return 'Hello'

greeting = say_hi()

print(greeting)
