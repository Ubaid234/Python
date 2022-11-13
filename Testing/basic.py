# Assertion 

# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# add_positive_numbers(1, 1) # 2
# add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive! 


def eat_junk(food):
    assert food in [
        'pizza',
        'ice cream',
        'candy',
        'fried butter'
    ],'Only junk food is allowed'
    return f"Nom Nom Nom I am eating {food}"

food = input("Enter a Food Please: ")
print(eat_junk(food))
