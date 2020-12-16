import time

gen_start = time.time()
print(sum(n for n in range(1000000000)))
gen_time = time.time() - gen_start




list_start = time.time()
print(sum([n for n in range(1000000000)]))
list_time = time.time() - list_start

print(f"generator expression took {gen_time} to run")
print(f"list comprehension took {list_time} to run")