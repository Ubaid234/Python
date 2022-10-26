#  sorted 
# Returns a new sorted list from the items in iterable 

more_numbers = [6,1,8,2]
print(sorted(more_numbers))
print(sorted(more_numbers , reverse=True))
print(sorted((2,1,45,23,99))) #works with tuple
print(more_numbers)

users = [

	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}

]

# print(sorted(users, key = lambda user: user['username']))
print(sorted(users, key = lambda user: len(user['tweets']), reverse=True))