class Aquatic :
    def __init__(self,name):
        print("AQUATIC INIT!")
        self.name = name 

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INT")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Ambulatory , Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT!")
        Ambulatory.__init__(self,name=name)
        Aquatic.__init__(self , name=name)

# jaws = Aquatic("jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("captain cook")

# print(captain_cook.swim())
# print(captain_cook.walk())
# print(captain_cook.greet()) 

# print(f"captain cook is instance of Penguin : {isinstance(captain_cook, Penguin)}")
# print(f"captain cook is instance of Penguin : {isinstance(captain_cook, Penguin)}")
# print(f"captain cook is instance of Penguin : {isinstance(captain_cook, Penguin)}")