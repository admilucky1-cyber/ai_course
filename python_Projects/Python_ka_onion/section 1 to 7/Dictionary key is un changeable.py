#dictionary key is unchangeable

# This will raise a TypeError because lists are mutable and cannot be used as dictionary keys.
characteristics = ['name', 'Power','bonus']
dictionary = {
    
    'player1': 'name',
    'power': 'full/100',
    'bonus': '2 lives',
}
print(dictionary)