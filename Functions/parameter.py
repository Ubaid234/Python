# single parameter

from regex import B


def square(num):
    return num * num

print(square(4))
print(square(8))

# multi Parameters

def multiply(first , second):
    return first * second

print(multiply(5,5))

# Naming parameters makes them sensefull

# Defualt parameters

def exponent(num, power = 2):
    return num ** power

print(exponent(2,3)) #8
print(exponent(3))

# An example without default values, if not provided values will give error
def add(a, b):
    return a + b 

# add() --> gives error

# With default parameters
def add(a = 10, b = 20):
    return a + b 

print(add())
print(add(1,2))


# Default Paramenters could be anything, Functions , lists , dictionaries , strings , booleans --all

def add(a, b): 
    return a + b

def math(a, b , fn= add):
    return fn(a,b)

def subtract(a,b):
    return a - b 

print(math(2,2))

print(math(2,2, subtract))


# Keyword Arguments

def full_name(first, last):
    return f"Your name is {first} {last}"

print(full_name(first= 'Colt' , last= 'Steele'))
print(full_name(last= 'Steele' , first= 'Colt'))
