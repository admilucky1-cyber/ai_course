#55.Exercise for loop
# target:print a table of two

list1 =[2]

list2 = [1,2,3,4,5,6,7,8,9,10]

for x in list1:
    for y in list2:
        result = x * y
        print(f"{x} x {y} = {result}")
#what does f" mean in print(f"")?
#The f in print(f"") stands for "formatted string literals" or "f-strings".
#It allows you to embed expressions inside string literals, using curly braces {}.
#When you prefix a string with f or F, you can include Python expressions inside the string by enclosing them in curly braces.
#When the string is printed, the expressions inside the curly braces are evaluated, and their values are inserted into the string at that position.
#For example:
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
#Output: My name is Alice and I am 30 years old.    
#In this example, {name} and {age} are expressions that get evaluated and replaced with their respective values when the string is printed.
#This makes f-strings a convenient way to create strings that include dynamic content.
#if i want to print 2-9 tables how can i do that?

list1 = [2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in list1:
    for y in list2:
        result = x * y
        print(f"{x} x {y} = {result}")
