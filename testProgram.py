import random
import sys
import os

print("Hello World")

# comment

''' 
this is a multiline comment
'''

name = "Dylan"
print(name)
'''
Data types (incomplete list) Numbers Strings Lists Tuuples Dictionaries
'''
name = 15

print (name)

'''
arithmatic
+ - * / % ** (exponential) // (/ with floor)
'''

print("5//2=",5//2)

quote = "\"Never give up never surrender\""

multi_line_quote=''' this is just
a tester '''

print("%s %s %s" %('I like a good quote', quote, multi_line_quote))

# printing without going to a new line

print('test',end=" ")
print("\n" *5)

#lists
grocery=['juice', 'lettuce', 'potatos'
	  'nanners']
other_events=['freakout', 'dont die', 'feed the carry']
print("First!", grocery[0])
print(grocery[1:3])

to_do_list = [grocery,other_events]
print(to_do_list)

print((to_do_list[1][1]))

#add items
grocery.append('Onions')

grocery.inster(1, "pickles")
#sort
grocery.sort()

grocery.reverse()
#del item
print(grocery)
del grocery[4]
print(grocery)

to_do_list2 = other_events + grocery
#lenth min max
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


print("/n" *5)


#tuples


