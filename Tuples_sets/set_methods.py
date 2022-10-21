# Set Methods

#add
from __future__ import annotations


s = set([1,2,3])
s.add(4)
print(s)

#remove
set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)
# set1.remove(3)
# print(set1) -- Gives error

#discard
set2 = {1,2,3,4,5}
set2.discard(2)
print(set2)
set2.discard(2) # --> Doesn't give any error
print(set2)

#copy
s = set([1,2,3])
another_s = s.copy()
print(another_s)
print(s is another_s)

#clear
s = set({1,2,3,4})
print(s.clear)

# Set Math (intersection, symmetric_difference, union)

math_students = {'Matthew', 'Helen' , 'Prashant', 'James' , 'Aparna'}
biology_students = {'Jane' , 'Matthew' , 'Charlotte', 'Mesut', 'Oliver' , 'James'}

# set union
print(math_students | biology_students)

# set intersection
print(math_students & biology_students)

