# Without Comprehension 

dict1 = {}
for n in range(10):
    dict1[n] = n*2
print(dict1)

# With comprehension 

dict2 = {n:n*2 for n in range(10)}
print(dict2)

# Without comprehension using condionals

dict1 = {}
for n in range(10):
    if(n%2==0):
        dict1[n] = n*2
print(dict1)

# With comprehension using condionals

dict2 = {n:n*2 for n in range(10) if n%2==0}
print(dict2)


# Nested ifs , without comprehension

dict1 = {}
for n in range(10):
    if(n%2==0):
        if(n%3==0):
            dict1[n] = n*2
print(dict1)

# Nested ifs with comprehension

dict2 = {n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict2)

# With Else , without comprehension

dict1 = {}
for n in range(10):
    if(n%2==0):
        dict1[n] = n
    else:
        dict1[n] = "invalid"
print(dict1)

# With comprehension using else

dict2 = {n:(n if n%2==0 else 'invalid') for n in range(10)}
print(dict2)



