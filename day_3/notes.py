
"""
1. Introduction to Python

Python is a high-level, interpreted programming language.
It's easy to read and write, widely used in data science, web development, and AI.


2. Python Variables

Variables store data values.
You don't need to declare the type explicitly; Python figures it out.

Example:

name = "Tejas"
age = 20
height = 5.9

Rules:

Must start with a letter or _.
Can contain letters, numbers, or _.
Case-sensitive (age ≠ Age).

3. Python Data Type

Data Type	Example	Description
int	age = 20	Integer numbers
float	height = 5.9	Decimal numbers
str	name = "Tejas"	Text
bool	is_student = True	True/False
list	marks = [90, 85, 95]	Ordered collection
tuple	coords = (10, 20)	Immutable ordered collection
dict	student = {"name": "Tejas", "age": 20}	Key-value pairs
set	fruits = {"apple", "banana"}	Unordered unique items

4. Input and Output

Input from user: input()
Print to console: print()

Example:

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert string to int
print("Hello", name, "you are", age, "years old")


Notes:

input() always returns string. Convert to int or float if needed.
print() can display multiple items separated by commas.


5. Simple Programs

Add two numbers:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum is:", sum)


Check if number is positive/negative:

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



6. Key Takeaways

Python is simple and beginner-friendly.

Variables store data and data types define the kind of data.

input() and print() are used for user interaction.

First programs are all about numbers, text, and basic conditions.

"""