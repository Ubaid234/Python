# all

# Return True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True

people = ['satar' , 'sesaw' , 'salim' , 'sahil','salik']

print(all([name[0]=='s' for name in people]))
print(all([name[1]=='s' for name in people]))

# any

# Return True if any element of the iterable is truthy. If the iterable is empty, return False.

any([0, 1, 2, 3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False

nums = [2,60,26,18,21]

print(all([num % 2 == 0 for num in nums])) #False
print(any([num % 2 == 1 for num in nums])) #True

