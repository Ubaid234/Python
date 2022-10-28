# Raise Your
# Own Exception!

# In python we can also throw errors using the raise keyword. This is helpful when creating your own kinds of exception and error messages.

# raise ValueError('invalid value')
# raise NameError("blah")


# usecase
def colorize(text, color):
    colors = ("cyan" , "yellow" , "blue" , "green" , "magenta")
    if type(color) is not str:
        raise TypeError('color must be instance of str')
    if type(text) is not str:
        raise TypeError('type must be instance of str')
    if color not in colors :
        raise ValueError("color is in invalid color")
    print(f'Printed {text} in {color}')

colorize('hello' , 10) 
# colorize(32 , 'red')

