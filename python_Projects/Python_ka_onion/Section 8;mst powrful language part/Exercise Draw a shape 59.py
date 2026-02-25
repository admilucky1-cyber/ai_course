#59::Draw a Shape
'''#Draw a rectangle

canvas = 10
inner_area = canvas - 2
print('x' * canvas)
print('x' + ' ' * inner_area + 'x')
for i in range(inner_area):
    print('x' + ' ' * inner_area + 'x') 
print('x'*canvas)'''
#draw a triangle using above method
'''
canvas = 10 #height and base of triangle
inner_area = canvas - 2 #area between the two edges of triangle
#print('x' * canvas)#prints top of triangle
for i in range(inner_area):
    print('x' + ' ' * i + 'x') #prints left and right edge of triangle
print('x' * canvas)#prints base of triangle
'''
#draw a diamond using above method
canvas = 10  # height of diamond
inner_area = canvas - 2  # area between the two edges of diamond

# Top tip of diamond
print(' ' * (canvas // 2) + 'x')

# Upper half
for i in range(inner_area // 2):
    print(' ' * (canvas // 2 - i - 1) + 'x' + ' ' * (2 * i) + 'x')

# Middle line
print('x' * canvas)

# Lower half (mirror of upper half)
for i in reversed(range(inner_area // 2)):
    print(' ' * (canvas // 2 - i - 1) + 'x' + ' ' * (2 * i) + 'x')

# Bottom tip of diamond
print(' ' * (canvas // 2) + 'x')


#
canvas = 11  # must be odd for symmetry

# Top half
for i in range(canvas // 2): # Iterate through each row#canvas // 2 means half of the total rows
    spaces = (canvas // 2 - i) * ' ' # Calculate leading spaces
    print(spaces + 'x' * (2 * i + 1)) # Print current row

# Middle line
print('x' * canvas)

# Bottom half
for i in reversed(range(canvas // 2)):
    spaces = (canvas // 2 - i) * ' '
    print(spaces + 'x' * (2 * i + 1))
