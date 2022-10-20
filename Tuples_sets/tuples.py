# Tuples 
# An Ordered collection or grouping of items

numbers = (1,2,3,4)
# It is immutable (can never b changed)
# numbers[0] = "change me" -- gives error
# Tuples r faster than lists

# Tuples are mostly used for unchanging date:
months = ['janaury' , 'february' , 'march' , 'april' , 'may' , 'june', 'july' , 'august' , 'september' , 'october' , 'november' , 'december']

# Access like lists 
print(months[0])

# Tuples can be used as keys in dictionaries 

locations = {
    (35.6895,39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New york Office",
    (37.7749, 122.4194): "San Fracisco Office"
}

print(locations[(37.7749, 122.4194)])

# Some dictionary methods like items() return tuples 

cat = {"name": "biscuit", "age":1 , "favourite toy": "my_chapstick"}
print(cat.items())