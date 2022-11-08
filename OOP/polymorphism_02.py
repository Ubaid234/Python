# Polymorphism & Inheritance

# 1. The same class method works in a similar way for different classes

# Each subclass will have a different implementation of the method.
# If the method is not implemented in the subclass, the version in the parent class is called instead.

# A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called method overriding.

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())



