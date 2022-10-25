# Parameter Ordering 

# 1. Parameter 
# 2. *args 
# 3. Default parameters 
# 4. **kwargs 

def display_info(a,b, *args , instructor ='colt', **kwargs):
    return [a, b, args , instructor , kwargs]

print(display_info(1,2,3, last_name = "steele" , job = " instructor "))