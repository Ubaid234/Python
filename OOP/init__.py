class user:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age 

user1 = user("Joe","smith", 68)
user2 = user("Blanca","Lopez", 41)
 
print(user1.first,user1.last)
print(user2.first,user2.last)
