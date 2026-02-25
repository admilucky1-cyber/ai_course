#53. video
# FOR LOOP AND ITERABLES::
#iterate means to visit each item of a collection one by one.
# for loop is used to iterate over a collection of items.
# Iterable is a collection of items that can be iterated over.

mylist = ["apple","banana","cherry","mango","milk"]
#print price tag of each item in the list
#print(mylist[0]+ ' price tag is 350')#accessing each item using index
#print(mylist[1]+ ' price tag is 100')#accessing each item using index
#print(mylist[2]+ ' price tag is 500')# accessing each item using index
#print(mylist[3]+ ' price tag is 250') #accessing each item using index
#print(mylist[4]+ ' price tag is 200')# accessing each item using index

'''print(next(mylist))
print(next(mylist)+ ' price tag is 350')
print(next(mylist)+ ' price tag is 100')
print(next(mylist)+ ' price tag is 500')
print(next(mylist)+ ' price tag is 250')
print(next(mylist)+ ' price tag is 200')'''#when we run this code it will give error because list is not an iterator
#to make a list an iterator we have to use iter() function
'''''
newlist = iter(mylist) #converting list to iterator
print(next(newlist)+ ' price tag is 350')#accessing each item using next()
print(next(newlist)+ ' price tag is 100')
print(next(newlist)+ ' price tag is 500')
print(next(newlist)+ ' price tag is 250')
print(next(newlist)+ ' price tag is 200')'''
#print(next(newlist))#if we run this line it will give error because there are no more items in the iterator
#we can use for loop to iterate over the list
#to automatically convert a list to an iterator and access each item one by one
for newlist in mylist:       #for loop is servent to iterate over a collection of items
    print(newlist)
    print(newlist+ 'price tag')
print('x'*20) 
newlist = iter(mylist) #converting list to iterator   
print(next(newlist)+ ' price tag ')
print(next(newlist)+ ' price tag ')
print(next(newlist)+ ' price tag ')
print(next(newlist)+ ' price tag ')
print(next(newlist)+ ' price tag ')
#print(next(newlist)+ ' price tag ')#if we run this line it will give error because there are no more items in the iterator
#for loop is more efficient and easier to use than using iter() and next() functions
###for loop can be used with any iterable object like list, tuple, string, dictionary, set etc.
#for loop is a servent to perform a task repeatedly until a certain condition is met.