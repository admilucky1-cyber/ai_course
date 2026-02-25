

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
mixed_numbers = [6,9,2,5,1,8,7,4,3]
items = ['mango', 'apple', 'banana', 'orange']
#print(numbers.count(5))  # Output: 2
#print(numbers.index(5))  # Output: 4
#print(items.index('banana', 0, 3)) #  # Output: 2
new_numbers = mixed_numbers.sort()
#print(new_numbers)  # Output: None  # because sort() modifies the list in place and returns None
mixed_numbers.reverse()
#print(mixed_numbers)  # Output: [3, 4, 7,
# 8, 1, 5, 2, 9, 6]
print(mixed_numbers)

