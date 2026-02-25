#44.dictionary key is unchangeable

# This will raise a TypeError because lists are mutable and cannot be used as dictionary keys.
characteristics = ['name', 'Power','bonus']
dictionary = {
    
    'player1': 'name',
    'power': 'full/100',
    'bonus': '2 lives',
    'player1': 'name',
    'power': 'full/100',
    'bonus': '2 lives',
}
#print(dictionary'bonus')  # Output: 2 lives])
print(dictionary.items())  # Output: None
#print('full/100'in dictionary.values())  # Output: True
print(dictionary.popitem())  # Output: dict_keys(['player1', 'power', 'bonus'])#LAST VALUE POP HOGI
#print(dictionary.clear())  # Output: None
#dictionary = {}  # This will clear the dictionary
#print(dictionary)  # Output: {}