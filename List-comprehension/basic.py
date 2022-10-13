# List comprehension 

numbers = [1,2,3,4,5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

name = ['colt']
capital = [char.upper() for char in name]
print(capital)

bro = ['sahil']
c_bro = [sahil.upper() for sahil in bro]
print(c_bro)

# With Ranges

tens = [nums * 10 for nums in range(1,6)]
print(tens)

# with bool for truthy or falsy

truth = [bool(val) for val in [0,[],'']]
print(truth)

# with str

nums = [1,2,3,4,5]
string_list = [str(num) for num in nums]
print(string_list)
string_list = [str(num)+ "Hello" for num in nums]
print(string_list)