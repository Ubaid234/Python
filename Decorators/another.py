from random import choice
# Inner functions can access outer function scope
def make_lauge_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHA", "LOL" , "HEHEHE"))
        return f"{laugh} {person}" 

    return get_laugh

laugh_at = make_lauge_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())