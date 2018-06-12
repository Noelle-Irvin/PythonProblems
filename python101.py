# Printing Stuff...
# By the way, ; are optional
# Python is an indented language, That means... indentation is VERY important
print "Test"
# print("Test"); This is only option in Python 3
#TO EXECUTE: ./python python101.py when in C:/Python27/ folder

print """
	Triple quotes will allow ou to type
	on multiple lines.
	It looks ugly, but is useful.
"""

# In Python, all variables are dynamically typed. Meaning...
# there is no int, String, [], etc. like JS Duck/dynamicalls typed
# To declare a variable in Python, just start using it.
# name = None;
name = "Noelle Irvin"

print "Hello, world, my name is %s" % name
print "Hello, world, my name is %s. Again, my name is %s" % (name, name)
# %s stands for String

age = 24
print "Hello, world, my name is %s, I am %d" % (name, age)
# %d stands for digit

# Python Data Types
#String - same old.
#Numbers - same old, with float and integers
print type(3.3) #this is a float
#Booleans = True, False (note capital)
print type(True) # this is a boolean

# lists = array
# dictionaries = JS object, key value pair
my_dictionary = {
	"name": "Noelle",
	"occupation": "Engineer"
}
print my_dictionary["name"] #bracket notation instead of dot notation
print my_dictionary["occupation"]

# Objects
# concatonate with the +
meaning_of_life = 42;
# print "The meaning of life" + meaning_of_life <- python won't allow us to do this
# You cannot concatonate disperate data types. You have to explicitly cast
print "The meaning of life " + str(meaning_of_life) #must turn into string

# Like in java, Strings are objects and therefore have methods
print "The meaning of life is {}".format(meaning_of_life)

# In Python, there is no auto-increment, no c++
counter = 1;
# counter++ <-this does not work
counter +=1 #this is how you must do it

# Conditionals
print 16 == "16" #this gives false

# As an indented language, you start ifs and fors with a colon(:)
# Everythin inside that block, is indented
if(16 == 16):
	print "16s are equal"
#elif is else if
#There is no ===
# to import modules
import random #Similar to require in node.js
#Python has pip and easy_install which are its package managers
# guess the number game
keep_playing = True
#this will give us a random number between 1 and 10
correct_number = random.randint(1, 10) 
while keep_playing:
	guess = int(raw_input("Guess a number between 1 and 10"))
	if(guess == correct_number):
		print "Hooray! You win a new car."
		keep_playing = False
	else:
		print "Try again"

#A list functions just like an array.
students = [
	"Branden",
	"Shahar",
	"Tawni",
	"Noelle",
	"Mariano",
	"Jos"
]

print students[0] #expect Branden to print out
#in python, a negative index, starts from the end and works backward
print students[-1] #will print out Jos

#push = append
students.append("Andrew")
print students[-1] #prints out Andrew
students.pop()
print students[-1] #Jos is end of array now

#range will create an array with each number
#range is inclusive of the first number, EXCLUSIVE of the second
#so the below is like saying int i = 0; i < 5. it does not include 5 but ends at 4
for i in range(0,len(students)):
	print students[i]

#lists have a sort method... sort MUTATES the list
students.sort()
print students
students.reverse() #this will sort them in reverse natural order
#sorted is a method that we hand an array but returns the sorted array, and 
#does not mutate it
print sorted(students) #this will give us same result as 109
print students

nameSplit = students[0].split("")
print nameSplit #
