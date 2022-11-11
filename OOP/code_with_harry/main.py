class Employee:
    def __init__(self , fname , lname , salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    pass

harry = Employee('Harry' , 'jacks' , 44000 )
rohan = Employee('Rohan' , 'das' , 44000)

print(harry.fname ,rohan.fname)