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
** Exponent

% Modulo/remainder

// Integer division/floor quotient

/ Division

* Multiplication

- Subtraction

+ Addition

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
        



## Error Handling

* SyntaxError: EOL while scanning string literal
* ZeroDivisionError: division by zero
* IndentationError: unexpected indent

