#While loop lecture 57
#while loop for infinite loop

#while condition:#its just a use of while it will not work if  you use word condition
 #   print('i run because condition is true')

#while True: #it will keep on running untill the condition is fasls or not true

#    print('i run because condition is true')
#x=True
#while x:
#    print('I Pray the Prayer because Allah Loves Me')
'''
x = True

print(bool(2 > 1))

while 2 > 1:
    print('I Pray the Prayer because Allah Loves Me')
    '''
#or

'''x = 2

y = 1

while x > y:
    print('I Pray the Prayer because Allah Loves Me')
'''

x = 10
y = 1
while x > y:
    print(f'I Pray the Prayer because Allah Loves Me {x}>{y} returns {x > y}')
    y= y+1
    print(y)











'''
#f'string  application on while loop
x = 10
y = 1
while x > y:
    print(f'I Pray the Prayer because, {x} >{y} returns {x > y}')
    y= y+1
    print(y)
    '''
x = 10
y = 1
while x > y:
    print(f'I Pray the Prayer because, {x} >{y} returns {bool(x > y)}')
    y += 1
    print(y)
else:
    print(f'I Pray the Prayer because, {x} >{y} returns {bool(x > y)}')       