#  46.Sets data Types
# A set is a collection which is unordered, unchangeable*, and unindexed.
# In Python sets are written with curly brackets.
#unique values/objects
#all operations can be done on sets as we can done on lists and tuples
test_set1 = {1,3,3,5,5,3,3,3,6,7,8,8,9,9}

test_set2 = {9,8,6,3,1}

print(test_set1.union(test_set2))  #combines both sets and removes duplicates
#print(test_set1.intersection(test_set2))  #returns only the values that are present in both sets
##print(test_set1.difference(test_set2))  #returns only the values that are present in the first set
#print(test_set1.symmetric_difference(test_set2))  #returns only the values that are not present in both sets   
#print(test_set1.issubset(test_set2))  #checks if all values in the first set are present in the second set
#print(test_set1.issuperset(test_set2))  #checks if all values in
#print(test_set1.isdisjoint(test_set2))  #checks if there are no values that are present in both sets
#print(test_set1.add(10))  #adds a value to the set
#print(test_set1.remove(3))  #removes a value from the set
#print(test_set1.pop())  #removes a random value from the set
#print(len(test_set1))  #returns the number of values in the set both sets are present in the first set
#print(test_set1.clear())  #removes all values from the set
#print(test_set1)  #prints the set
#print(type(test_set1))  #prints the type of the set
#print(test_set1)  #prints the set
#print(test_set2)  #prints the set
