# Scope 
# Variable created in functions are scoped in that function!

instructor1 = 'Colt' # -- > Global variable

def say_hello():
    return f"Hello {instructor1} " 

print(say_hello())

# Variable scoping

def say_hello():
    instructor2 = 'Colt'
    return f'Hello {instructor2}'

say_hello()

# print(instructor2) -- . NameError

# Global
total = 0

def increment():
    total += 1
    return total 

# increment() -- > error

# To overcome the above problem , we use the keyword global within the function 

total = 0

def increment():
    global total
    total += 1
    return total 

print(increment())

# nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1 
        return count
    return inner()

print(outer())