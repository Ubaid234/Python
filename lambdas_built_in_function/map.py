# map 

# A standard function that accepts at least two arguments, a function and an "iterable"

# iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

nums = [1,2,3,4,5]

def double(x): return x * 2 

doubles = list(map(lambda x : x * 2 , nums)) # these two doubles do the exact same thing but in this one , we use lambda with map which is common use-case for them.

doubles = list(map(double, nums)) # here we use it map with a defined function.
print(doubles)