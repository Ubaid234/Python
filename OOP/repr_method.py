# The __repr__ method is one of several ways to provide a nicer string representation:

class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name
        
dude = Human()
print(dude)  # "somebody"
colt = Human(name="colt steele")
print(f"{colt} is totally red (probably)")


# There are also several other dunders to return classes in string formats (notably __str__ and __format__), and choosing one is a bit complicated!



