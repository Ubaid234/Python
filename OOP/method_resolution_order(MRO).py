# Method Resolution Order (MRO)

# Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.

# You can programmatically reference the MRO three ways:

# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method

class A:
    def do_something(self):
        print("Method Define in: A")

class B(A):
    def do_something(self):
        print("Method Defined in: C")

class C(A):
    def do_something(self):
        print("Method Defined in: C")

class D(B,C):
    def do_something(self):
        print("Method Defined in: D")
        super().do_something()

# print(D.mro())
# help(D)
# print(D.__mro__) 
thing = D()
thing.do_something()



#     A
#    / \    
#    B  C
#    \ /
#     D