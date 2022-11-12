from random import choice
# we can return funcs from other funcs

def make_lauge_func():
    def get_laugh():
        l = choice(("HAHAHA", "LOL" , "HEHEHE"))
        return l 

    return get_laugh

laugh = make_lauge_func()
print(laugh())