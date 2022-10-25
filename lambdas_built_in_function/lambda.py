def square(num) : 
    return num * num 

square2 = lambda num: num * num 

add = lambda a,b : a + b

print(square(9))
print(square2(9))
print(add(2,3))

print(square.__name__)
print(square2.__name__)
print(add.__name__)
