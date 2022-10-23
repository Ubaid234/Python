# **kwargs
# Gathers remaining keyword arguments as a dictionary

def fav_colors(**kwargs):
    print(kwargs)

print(fav_colors(colt = "purple" , ruby = "red" , ethel = "teal"))

# modifying the above function

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite color is {color}")

print(fav_colors(colt = 'purple' , ruby = 'red' , ethel = 'teal'))
print(fav_colors(colt = 'purple' , ruby = 'red' , ethel = 'teal', ted = 'blue'))
fav_colors(colt = 'royal deep amazing purple')


