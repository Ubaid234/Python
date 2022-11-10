import time

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_stop = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(100000)) took: {gen_stop}")
print(f"sum([n for n in range(100000)]) took: {list_time}")
