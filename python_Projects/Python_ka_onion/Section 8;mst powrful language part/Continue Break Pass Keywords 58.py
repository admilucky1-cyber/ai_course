#58::Continue Break Pass Keywords
##01: Continue and Break Keywords in While Loop
'''
x = 10

y = 1

while x > y:
    print(f'I Pray the Prayer because, {x} >{y} returns {bool(x > y)}')
    #break# to exit the loop
    #continue# to skip the current iteration and continue with the next one
    y += 1
    print(y)
else:
    print(f'I Pray the Prayer because, {x} >{y} returns {bool(x > y)}')


#that code is not ready for execution yet
#i need to implement it later # i need this for loop
# The 'pass' statement is used as a placeholder. It does nothing and is used when a statement is syntactically required but no action is needed.
# Example:
for i in range(10):
    pass  # Placeholder for future code
# In this example, the loop iterates over a range of numbers but does not perform any action because of the 'pass' statement.
'''
#while loop for number of times with condition using command
#when i dont know how many times the loop will run then while loop is used/best and if i want to run for number of times then for loop is used/best

#while loop or infinite loop

while True:
    command = input('Please say yes: ')
    if command == 'yes':
        
        break  # Exit the loop when the user says 'yes'