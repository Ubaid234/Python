# filter

    # There is a lambda for each value in the iterable.

    # Returns filter object which can be converted into other iterables

    # The object contains only the values that return true to the lambda

list1 = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0 , list1))
print(evens)

users = [

	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}

]

inactive_users = list(filter (lambda u: len(u['tweets']) == 0 , users))

inactive_users = list(filter (lambda u: u['tweets'] , users))

inactive_users = list(filter (lambda u:not u['tweets'] , users))

print(inactive_users)

# Combining filter and map

usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda u: not u['tweets'], users)))
print(usernames)

# Given this list of names:

names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string
# "Your instructor is " + each value in the array,
# but only if the value is less than 5 characters

combo = list(map(lambda name: f"Your instructor is {name}",
     filter(lambda value: len(value) < 5, names)))

# ['Your instructor is Colt']
print(combo)

# List Comprehension 

names = ['Lassie', 'Colt', 'Rusty']

# using list comprehension to get exactly the same value as above 

combo2 = [f"Your instructor is {name}" for name in names if len(name) < 5]

print(combo2)
