# Generators

#  Generators are iterators
#  Generators can be created with generator functions
#  Generator functions use the yield keyword
#  Generators can be created with generator expressions

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(8)
print(next(counter))