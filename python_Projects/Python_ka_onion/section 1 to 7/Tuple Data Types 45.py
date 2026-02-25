#  45.Tuple Data Types
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#inside a dictionary

dictionary = {
    
    'player1': 'name',
    'power': 'full/100',
    'bonus': '2 lives',
}
#1st example of tuple#  
#test_tuple = (1, 2, 3)
#test_tuple[0] = 4  # This will raise a TypeError because tuples are immutable
#print(test_tuple)
# 2nd example of tuple unpacking   
#test_tuple = (1, 2, 3)
#a,b,c = test_tuple
#print(a)  # Output: 1
#print(b)  # Output: 2
#print(c)  # Output: 3

# 3rd example of tuple inside a dictionary
# Accessing tuple elements
#test_tuple = (1, 2, 3)

#print(2 in test_tuple)  # Output: True
#print(200 in test_tuple)  # Output: False

# 4th example of tuple inside a dictionary

test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#print(len(test_tuple))  # Output: 10
print(min(test_tuple))  # Output: 1
print(max(test_tuple))  # Output: 10
print(sum(test_tuple))  # Output: 55
print(sorted(test_tuple))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(reversed(test_tuple)))  # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(test_tuple.count(5))  # Output: 1 # Count of occurrences=how many times repeated of 5
print(test_tuple.index(7))  # Output: 6# Index of first occurrence of 7
print(test_tuple.index(1))  # Output: 0# Index of first occurrence of 1
print(test_tuple.index(10))  # Output: 9# Index of first occurrence of 10
print(test_tuple[2:5])  # Output: (3, 4, 5)#slicing #3rd index se 5th index tak print hoga
print(test_tuple[:4])  # Output: (1, 2, 3, 4)#starting se 4th index tak print hoga
print(test_tuple[6:])  # Output: (7, 8, 9, 10)#6th index se end tak print hoga  
print(test_tuple[-4:])  # Output: (7, 8, 9, 10)#last se 4th index tak print hoga
print(test_tuple[:-6])  # Output: (1, 2, 3, 4)#starting se last ke 6th index tak print hoga
print(test_tuple[::-1])  # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)#reverse order print hoga#test_tuple[start:stop:step]start and stop are omitted → entire tuple step = -1 → traverse in reverse order
#print(test_tuple[::2])  # Output: (1, 3, 5, 7, 9)#test_tuple[start:stop:step] is the general slicing syntaxstart and stop are omitted, so it defaults to the entire tuple.
#step=2 means it selects every second element, starting from index 0.
print(test_tuple[1::2])  # Output: (2, 4, 6, 8, 10)#test_tuple[start:stop:step] is the general slicing syntaxstart=1 means it starts from index 1stop is omitted, so it defaults to the end of the tuplestep=2 means it selects every second element starting from index 1
# Note: Tuples are immutable, so methods that modify the tuple (like append, remove, etc.) are not available.
# Tuples can contain elements of different data types, including other tuples.
