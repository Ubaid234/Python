# LC with conditional logic

numbers = [1,2,3,4,5,6]

# IF
evens = [num for num in numbers if num % 2 == 0]
print(evens)
odds = [num for num in numbers if num % 2 != 0 ]
print(odds)

# Else
if_else = [num*2 if num % 2 == 0 else num/2 for num in numbers ]
print(if_else)

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels if char not in "aeiou"))
