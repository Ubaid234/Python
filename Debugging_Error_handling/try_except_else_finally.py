# try: 
# except:
# else:
# finally:

# try: 
#     num = int(input("please enter a number:"))
# except:
#     print("That's not a number")
# else:
#     print("I'm in the else")
# finally:
#     print("Runs No Matter What")


# while True:
#     try: 
#         num = int(input("please enter a number:"))
#     except ValueError:
#         print("That's not a number")
#     else:
#         print("Good job, you entered a number")
#         break
#     finally:
#         print("Runs No Matter What")
# print("Rest of game logic runs")

def divide (a,b):
    try:
        result = a/b 
    except ZeroDivisionError:
        print("Don't divide by zero please")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else :
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,'a'))