# Built in Modules

import random

print(random.choice(["apple", "banana", "cherry", "durian"]))
print(random.randint(1, 50))
random.shuffle(["apple", "banana", "cherry", "durian"])

import random as r

r.choice(["apple", "banana", "cherry", "durian"])
r.shuffle(["apple", "banana", "cherry", "durian"])

# Importing Parts of a Module 

from random import choice,randint

print(choice(["apple", "banana", "cherry", "durian"]))
print(randint(1, 50))

from random import choice as pick, randint as random_number

print(pick(["apple", "banana", "cherry", "durian"]))
print(random_number(1, 50))


# Different Ways to Import

# import random

# import random as omg_so_random

# from random import *

# from random import choice, shuffle

# from random import choice as gimme_one, shuffle as mix_up_fruits
