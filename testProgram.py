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

print("\n" *5)
print("lists")
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

grocery.insert(1, "pickles")
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


print("\n" *5)


#tuples
#cannot be changed after created
print('tuples')
pi_tuple= (3,1,4,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

len(pi_tuple)
max(pi_tuple)
min(pi_tuple)

#dictionaries or maps
print("dictionaries")
#		     key    :   value
super_villains = {'Fiddler' : 'Isaac Bowin',
			'Captain Cold' : 'Leonard Snart',
			'Weather Wizared' : 'Mark Mardon',
			'Mirror Master' : 'Sam Scudder',
			'Pied Piper' : 'Thomas Peterson',
		}

print(super_villains['Captain Cold'])
del super_villains['Mirror Master']
super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))
print(super_villains.get("Pied Piper"))
print(super_villains.keys())
print(super_villains.values())
print("\n" *5)

#if else elif == != > >= < <=
#white space used
print("conditionals")
age = 21
if age > 16:
	print('You are old enough to drive')
else :
	print('Youre too fkn young')

if age >= 21:
	print('You are not odl enough to drink')
elif age>=16:
	print('Still too young')
else :
	print('Way to young')

#operators and or not

if ((age >= 1) and (age <= 18)) :
	print('You get sumfin gud')
elif ((age == 21) or (age >= 65)):
	print('Get out of here young one')
elif not(age == 30):
	print('Get on mah level')
else:
	print('Go Shawty its yo birfday')

print("\n"*5)


#looping
print('looping')
for x in range(1,10):
	print(x, ' ')

print("\n")

for y in grocery:
	print(y)

for x in [2,4,6,8,10]:
	print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3): #up to but dont include 3
 for y in range(0,3):
	print(num_list[x][y])

#WHILE LOOPS

random_num = random.randrange(0,7) # 0 to 99
while (random_num != 5):
	print(random_num)
	random_num = random.randrange(0,7)

i = 0

while(i <= 20):
	if(i%2 ==0):
		print(i)
	elif(i == 9):
		break  #breaks loop
	else:
		i += 1
		continue #jumps to top of loop
	i += 1

print('\n'*5)

#functions
print('Fucntions')
def addNumber(fNum, lNum):
	sumNum = fNum + lNum
	return sumNum

print(addNumber(1,4))

#get input from user

print('Put in yo name: ')
name = sys.stdin.readline()

print('Hello', name)

print('\n'*5)




#strings
print('strings')
long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[-5:]) #lst 5 characters

print(long_string[:-5]) #all but last 5

print(long_string[:4] + " be there")
     #char      #string                 #int            #float with 5 places                   
print("%c is my %s letter and my number %d number and %.5f"%('X', 'favorite', 1, .14))

print(long_string.capitalize())

print(long_string.find("Floor"))

print(long_string.isalpha()) #all letters?

print(long_string.isalnum()) #all nums?

print(len(long_string))

#print(long_string.replace("Floor", "Ground"))

print(long_string.strip()) #strip white space

word_listing = long_string.split(" ")

print(word_listing)

print('\n'*5)

#using files
print('using files')
test_file = open("test.txt", "wb") #wb is write
print(test_file.mode) #mode, this is in wb

print(test_file.name) #name of file

test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open("test.txt", "r+") #open for reading

text_in_file = test_file.read() #read file
print(text_in_file)

os.remove("test.txt")

print('\n'*5)

#objects
print('objects')
class Animal:
	__name = None
	__height = 0
	__weight = 0
	__sound = 0   #__ means private, need function to modify

	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = name
		self.__weight = weight
		self.__sound = sound

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_weight(self, weight):
		self.__weight = weight 

	def get_weight(self):
		return self.__weight

	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
										self.__height,
										self.__height,
										self.__weight,
										self.__sound)

cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())

	#inheritance, get all variables 

class Dog(Animal):
	__owner = ""

	def __init__(self, name, height, weight, sound, owner):
		selfl__owner = owner
		super(Dog, self).__init__(name, height, weight, sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString(self): #override
		return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
										self.__height,
										self.__height,
										self.__weight,
										self.__sound,
										self.__owner)
					#ok not to send value
	def multiple_sounds(self, how_many=None):
		if how_many is None:
			print(self.get_sound())
		else:
			print(self.get_sound() * how_many)

	
spot = Dog("spot", 53, 27, "Ruff", "Dylan")
#poly morphism
print(spot.toString())
		
class AnimalTesting:
	def get_type(self, animal):
		animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds()
spot.multiple_sounds(4)
