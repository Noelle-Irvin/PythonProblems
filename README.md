# Python Syntax Cheat Sheet

To write a **comment** in python use the hash tag at the start of the line: 
   
    # This is a comment.
    
To **print** use the keyword *print*():

    print("Hello World!")
    
**Important**: Python utilizes proper spacing to distinguish blocks of code

Python uses a *tab* or *4 spaces* to contain code in a code block. The example below prints "Hello, World!" 100 times.

    for i in range(100):
        print("Hello, World!")
        
## Data Types
* string - str, ex: "This is a string"
* integer - int, ex: 10
* floating-point number - float, ex: 2.22
* booleans - bool, ex: True
* NonType - where None is the value

Python does not require you to specify the type when making variable declarations.

    x = 100
   
>>100

Here x is assigned the value of 100.

#### Increment
    x = 10
    x = x + 1
    print(x)
>>11
    
OR

    x = 10
    x += 1
    print(x)
>>11

## Arithmatic Operators
'**' Exponent

'%' Modulo/remainder

'//' Integer division/floor quotient

'/' Division

'*' Multiplication

'-' Subtraction

'+ 'Addition

## Comparison Operators

'>' Greater Than

'<' Less Than

'>=' Greater than or equal to

'<=' Less than or equal to

'==' Equal

'!=' Not Equal

## Logical Operators

and - True and True -> True

or - True or False -> True

not - not True -> False

## Conditional Statements
Conditional statements can be constructed with keywords: *if*, *elif* & *else*

Given x = 3. The following conditional statment would yield 
>x is not 1 or 2

    if x == 1:
        print("x is 1")
    elif x == 2:
        print("x is 2")
    else:
        print("x is not 1 or 2")
        

## Functions

Use keyword *def* to define your function and then give your function a name along with parameters to pass in parenthesis

    def functionName(x):
        return x + 1
        

    functionName(2)
>> 3

## Built-in Functions

* len() - returns the length of the object passed to it

* str() - returns the object that gets passed to it as a string

* int () - returns the object that gets passed to it as a integer

* float() - returns the object that gets passed to it as a float

* input(x) - prints x to the console; pauses program; takes in a string that is typed into console

## Required and Optional Parameters

Python lets you set optional parameters in a function by giving the optional parameter a default value

    def functionName(x, y = 2):
        return x + y

Here x is required and y is optional.

    functionName(1, 4)
>>5
    
    functionName(1)
>>3


## Variable Scope

**Global Variable** - a variable with global scope that can be read or written to from anywhere in your program

**Local Variable** - a variable with local scope that can only be read or written to from within the function or class that it is in

Use keyword *global* when writing to a global variable from within a function 

    x = 2
    
    def f():
        global x
        x += 1
        print(x)
        
    f()
>>3
 

## Error Handling

    y = input("Give a value for y:")
    
    try:
        x = int(y)
    except ValueError:
        print("y must be a number")
        
>>Give a value for y:

>>Python

>>y must be a number


Python Exceptions:

* SyntaxError: EOL while scanning string literal
* ZeroDivisionError: division by zero
* IndentationError: unexpected indent
* ValueError: invalid literal for int() with base 10: 'exampleString'

## Containers

### Lists
* a container that stores objects in a specific order
* iterable
* mutable

    
    list = []
    list = list()
    
use index such as list[1] to find object in the list at a specific index

use *append()* to add to a list

use *pop()* to remove last item from list

add 2 lists with the addition operator

use keyword *in* to check if an item is in a list

use keyword *not* paired with *in* to check if an item is not in a list

### Tuples
* a container that stores objects in a specific order
* immutable
* iterable


    tuple = ()
    tuple = tuple()
    
use index such as tuple[1] to find object in the tuple at a specific index

use keywords *in* and *not* just like lists


### Dictionaries

* a container that maps a key to a value

    
    dictionary = {}
    dictionary = dict()
    
add a value using the following format:

    dictionary["key1"] = "value1"
    dictionary["key2"] = "value2"
    
>>{"key1":"value1", "key2":"value2"}

use keywords *in* and *not* just like lists

Containers can contain different containers.

## Strings

* strings are immutable
* use an index to look up a character, indexes start at 0
* a **negative index** can be used to look up items from right to left where [-1] gives the last character in a string

    
    string = "Jenaba"
    string[0] = J
    string[2] = n
    string[-1] = a
    string[-2] = b

* triple quotes can be used to surround a string that has multiple lines

    
    string = """line 1
                line 2
                line 3
            """
    
* use '+' to add strings together

    
    "string1" + "string2" 
    
    
>>"string1string2" 
        
* use the asterisk to multiply strings

    "string1" * 2
    
>> "string1string1"

#### Built-in Functions for Strings

**.upper()** - turns string to all upper case characters

**.lower()** - turns string to all lower case characters

**.capitalize()** - capitalizes the first letter of a sentence

**.format(x)** - will insert into the string to replace the empty {}

    
            "Hello, my name is {}".format("Noelle")
    
>> "Hello, my name is Noelle"


**.split(x)** - splits a string into a list at each x

    "blue, pink, purple".split(", ")
    
>> ["blue", "pink", "purple"]

**.join()** - used to add new characters between characters of a string; can also be used to turn a list of strings into a string with a new character in between

    ".".join("python")
    
>> "p.y.t.h.o.n"

    listOfStrings = ["blue", "pink", "purple"]
    newString = " ".join(listOfStrings)
    
>> "blue pink purple"

**.strip()** - strips string of excess white space

    string = "      python    "
    string.strip()
    
>> "python"

**.replace(x, y)** - when passed two arguments x & y, will replace x with y

    string = "Hello World"
    string.replace("l", "!")
    
>> "He!!o Wor!d"

**.index(x)** - returns the index of the first occurrence of x in a string

    string = "Hello World"
    string.index('o')
    
>> 4

* use the keyword *in*  to check if a string contains another string

* escape strings within strings by using the backslash (\")

    "I said \"Hello World\""
    

* \n in a string creates a new line

* use the syntax string[x:y] to slice a string from index x up to index y

    
    string = "Hello World"
    string[0: 5]
    
>> "Hello"

- slicing can be used on Lists as well

## Loops

#### For-Loop

* for-loops are used to iterate through an iterable (string, list, etc.)

       name = "Ted"
       for character in name:
            print(character)
>T
>e
>d
  
 * you can also have an index variable in a for-loop by using enumerate(x):
 
    
    tv = ["GOT", "Narcos", "Vice"]
    for i, show in enumerate(tv):
        new = tv[i]
        new = new.upper()
        tv[i] = new
        
    print(tv)
    
>> ['GOT', 'NARCOS', 'VICE']

* or by using range(x,y):

        
    for i in range(1, 11):
        print(i)
        
>> 1

...

>> 9 
>> 10   

#### While-Loop

* while-loops are used to run a block of code as long as a condition is true

    
    x = 3
    while x > 0:
        print(x)
        x -= 1
    print("Happy New Year!")
    
>>3

>>2

>>1

>> 'Happy New Year!'

* **Note:** writing 'while True:' will make an infinite loop unless you use a break statement

#####Break

* a break statement is used to terminate a loop


    while True:
        a = input("Guess a number: ")
        if a == '87':
            break
        else
            print("That's not the right number!"

#####Continue

* a continue statement stops the current iteration & moves onto the next one


    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
        
>> 1

>> 2

>> 4

>> 5


#### Nested Loops

* you can combine loops by putting, or 'nesting', one loop inside another

    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    added = []
    for i in list1:
        for j in list2:
            added.append(i + j)
            
    print(added)
    
>> [5, 6, 7, 6, 7, 8, 7, 8, 9]


### Modules

* another name for a python file with code in it

* you can import a module using keyword *import* to use variables and functions from it

**Built-in Modules:**

* math

* random

* statistics

* keyword


    import math
    
    math.pow(2, 3)
    
>> 8.0

**Create your own module by:**

* create a python file

* save the file

* import the file into another file located in the same folder

### Files

* python has built-in functions made to manipulate file objects

* first step is to open a file using the *open()* function

* the *write(x)* function lets you write x to a file

* the *read()* function lets you read from a file

* you must close a file with the *close()* function

#### Open file

* the *open* function takes a file and a file mode and returns a file object

* Here are some modes that you can open a file in :
    * "r" - opens a file for reading only
    * "w" - opens a file for writing only; overwrites the file if it already exists; if it doesn't exist, creates a new file
    * "w+" - opens a file for reading and writing; overwrites the file if it already exists; if it doesn't exist, creates a new file
    

    st = open("st.text", "w")
    st.write("Hi from Python!")
    st.close()
    
#### Automatically close file

* to automatically close a file without using the *close() function, open your file using a **with-statement**


    with open("st.txt", "w") as f:
        f.write("Hi from Python!")
        
* this will automatically close the file once the code inside the with-statement executes

#### CSV files

* python has built-in module for working with CSV files

* you can use the *open()* function to open a file and then use the *writer()* function from the csv module to turn the file object into a csv object

* use the function *writerow()* to write to the csv object

    
    import csv 
    
    with open("st.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(["one", "two", "three"])
        w.writerow(["four", "five", "six"])
        
>> one,two,three

>>four,five,six

* the csv module also has a function for reading a CSV file: *reader()*
* the *reader()* function returns an iterable of the rows in the csv file

   
    import csv
    
    with open("st.csv", "r") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            print(",".join(row))
                
>> one,two,three

>> four,five,six