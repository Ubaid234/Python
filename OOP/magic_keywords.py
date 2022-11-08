# Special Methods

# Python classes have special (also known as "magic") methods, that are dunders (i.e. double underscore-named).

8 + 2  # 10
"8" + "2"  # 82

# 2. (Polymorphism) The same operation works for different kinds of objects

# How does the following work in Python?

# The answer is "special methods"!

# These are methods with special names that give instructions to Python for how to deal with objects.

# what is happening ?

# The + operator is shorthand for a special method called __add__() that gets called on the first operand.

# If the first (left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatenation


from copy import copy
class Human:

    def __init__(self,first, last ,age):
        self.first = first
        self.last = last
        self.age = age 

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age 

    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that"

    def __mul__(self,other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't Multiply"
        

j = Human("Jenny" , "Larsen" , 47)
k = Human("Kevin" , "Jones" , 49)
# print(j)
# print(len(j))

# print(j * 3) 
triplets = j * 3
triplets[1].first = 'Jessica'
# print(triplets)

triplets = (k + j )* 3
# Kevin and jessica having triplets
print(triplets)