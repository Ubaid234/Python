# *Args
# Gathers remaining arguments as a tuple

def sum_all_values(*args):
    total = 0 
    for val in args:
        total += val

    return total 

print(sum_all_values(1,2,3,4))
print(sum_all_values(2,3,4,5,5,3,2,1,4,))

# Another example 

def ensure_correct_info(*args):
    if "colt" in args and 'steele' in args :
        return 'welcome back Colt'

    return "Not sure who you are..."

print(ensure_correct_info('hello' , False , 76))
print(ensure_correct_info(1,True, 'steele' , 'colt'))