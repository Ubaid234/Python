# Accessing individual values 

instructor = {
    "name": "colt",
    "owns_dog" : True,
    "num_courses": 4,
    "favourite_language": "python",
    "from" : "US",
    "insert more" : "here"
}

print(instructor["name"])
print(instructor["from"])

# Accessing all Values in a Dictionary

for value in instructor.values():
    print(value)

# Accessing all Keys in a Dictionary

for v in instructor.keys():
    print(v)

# Accessing all Values and keys in a Dictionary

for data,values in instructor.items():
    print(f"key is {data} and value is {values}")