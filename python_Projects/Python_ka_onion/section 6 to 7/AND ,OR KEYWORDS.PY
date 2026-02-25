#49.AND OR KEYWORDS
#an
#or
# In Python, the keywords 'and' and 'or' are used to combine conditional statements.
# The 'and' keyword returns True if both conditions are true, while the 'or' keyword returns True if at least one condition is true.
cat = True
dog = True

owner = True

if cat or dog:
    print('Mouse Run Away')
elif owner:      
        print('owner is present')
else:
    print('Mouse Eat Cheese')
#2nd case when cat is false/not present but owner is true/present    
cat =  False
dog = True
owner = True

if cat or dog:
    print('Mouse Run Away')
elif owner:      
        print('owner is present')
else:
    print('Mouse Eat Cheese')
#3rd case when both are false/not present
cat = False 
dog = False
owner = False
if cat or dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
"""
#Using AND keyword
cat = True
dog = True
owner = True
if cat and dog:
    print('Mouse Run Away')
elif owner:      
        print('owner is present')
else:
    print('Mouse Eat Cheese')
#2nd case when cat is false/not present but owner is true/present    
cat =  False
dog = True
owner = True
if cat and dog:
    print('Mouse Run Away')
elif owner:      
        print('owner is present')
else:
    print('Mouse Eat Cheese')
#3rd case when both are false/not present
cat = False
dog = False
owner = False
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
#4th case when both are true/present
cat = True 
dog = True
owner = False
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')   
else:
    print('Mouse Eat Cheese')
#5th case when cat is true/present but dog is false/not present
cat = True
dog = False
owner = False
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
#6th case when dog is true/present but cat is false/not present
cat = False
dog = True
owner = False
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
#7th case when both are false/not present but owner is true/present
cat = False
dog = False
owner = True
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
#8th case when all are true/present
cat = True 
dog = True
owner = True
if cat and dog:
    print('Mouse Run Away')
elif owner:
    print('owner is present')
else:
    print('Mouse Eat Cheese')
"""