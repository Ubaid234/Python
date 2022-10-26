import sys 
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f'Generator Expression: {list_comp} bytes') # 8846 bytes
print(f'Generator Expression: {gen_exp} bytes') # 104 bytes