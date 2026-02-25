#Dictionary in python# defines key value pairs
#defining a dictionary#
dictionary = {'key1':[1,2,3],'key2':True,'key3':'i sm string'}#whatever is in {} is dictionary
#print(dictionary)
#printing value of a key
print(dictionary['key1'][2])#prints 3rd element of list at key1

mixed_dict = [{'key1':[7,9,8],'key2':True,'key3':'i sm string'},{'key1':['a','c',3],'key2':False,'key3':'i sm string'},{'key1':['a','b',3],'key2':True,'key3':'i sm string','key4':(1,2,3)}]#list of dictionaries
print(mixed_dict[2]['key3'][0:1])#prints 'b' from 3rd dictionary in list