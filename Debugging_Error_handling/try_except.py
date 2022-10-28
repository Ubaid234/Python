# Handle error 

# In Python, it is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them. Let's see what that looks like.

# try: 
#     foobar
# except:
#     print("Problem")
# print("after the try")

def get(d,key): 
    try:
        d[key]
    except KeyError: 
        return None
d = {"name" : "Ricky"}
print(get(d, "city"))
d["city"]
  