# Decorator Syntax 

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt.")

@be_polite
def rage():
    print("I HATE YOU")

greet()
rage()

# we don't need to set 
# greet = be_polite(greet)