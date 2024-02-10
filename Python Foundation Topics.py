#Python Foundation #Author: Gina Rubik 
# For quick run of example codes use this online compiler: https://www.programiz.com/python-programming/online-compiler/

# Useful shortcuts:
# Highlight multiple lines or 1 line which you want to comment then press CTRL + /ctrl + k + c and ctrl + k + u to uncomment


#1. Data Types: provide a foundation for creating well-organized and flexible code in an object-oriented manner

#1.1. Primitive Data Types: Integers, Floats, Booleans, Strings are basic building blocks of data

num = 10
float_num = 3.14
boolean = True
string = "Hello, World!"

#1.2.Composite Data Types: Lists, Tuples, Sets, and Dictionaries are used to store collections of data

my_list = [1, 2, 3, 4]    #square brackets
my_tuple = (1, 2, 3)      #round brackets 
my_set = {1, 2, 3}        #curly brackets 
my_dict = {'key': 'value', 'name': 'John'} #curly brackets with key value pairs using semi colon and comma for separation

#1.3.Special Data Types: 

#NoneType represents the absence of a value

none_value = None

#Collections: specialized container data types with efficient solutions for various data manipulation tasks, providing specialized features beyond basic data structures

my_list = [1, 2, 3, 1, 2, 3, 4, 1, 2, 1]
element_counts = Counter(my_list)
for element, count in element_counts.items():
    print(f"Element {element} occurs {count} times.") #counting occurence of an element 

#1.4.Type Conversion: between different data types using functions like int(), float(), str(), etc.

num_str = "42"
num_int = int(num_str)  # Converts string to integer

#2. Strings: ordered and immutable sequence of characters. created using single or double quotes (' or ")                                    

my_string = "Hello, World!"
print(my_string)

Output: Hello, World!

#3. Variables: names used to store data values

x = 10
print(x)

10

#4. Loops: repeated execution of statement sets
#for loop:
for i in range(5):
    print(i)       # important! 4 indents

0
1
2
3
4

# while loop: to print numbers from 1 to 5 (inclusive)
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 #continue printing incremented by 1 until counter hits number 5, then program will stop 
1
2
3
5   

#5. Functions: a block of reusable code
    
def greet(name):
    print(f"Hello, {name}!")

greet("Name")  #call function

Hello, Name!

#6. Operators: symbols that perform operations on variables and values

x = 10
y = 3
result = x / y        #division operator
print(result)

3.3333333333333335    #output is a decimal 

#6. If Statements: conditional execution of code

age = 21
if age <= 21:     #smaller or equal than 
    print("You are a child!") #indentation is important

You are a child!


#Basic Data Structures:

#7. Lists: ordered, mutable(changeable) collection of elements (items) created by using square brackets [].
#Used to store collections of items of any data type, making them suitable for managing ordered sequences of elements
    
my_list = [1, 2, 3, 4, 5] or for example my_list = [1, 2, 3, 'four']

#List Manipulations:

#Accessing elements by their index

print("First element:", my_list[0])  #first index is zero
print("Last element:", my_list[-1])  #first index from rear

First element: 1
Last element: 5

#7.1.Appending an element: adding it to the last place of the list

my_list.append(6)
print("After appending 6:", my_list)

After appending 6: [1, 2, 3, 4, 5, 6]

#7.2.Inserting an element at a specific index

my_list.insert(2, 7)
print("After inserting 7 at index 2:", my_list)

After inserting 7 at index 2: [1, 2, 7, 3, 4, 5, 6]

#7.2 Removing Elements:

my_list = [1, 2, 3, 4, 5]

#7.2.1 Removing an element by value

my_list.remove(3)
print("After removing 3:", my_list)

After removing 3: [1, 2, 4, 5]

#7.2.2. Removing an element by index

del my_list[1]  #use a delete function to remove value 2 from index 1 position of our list of which 3 was previously removed
print("After removing element at index 1:", my_list)

After removing element at index 1: [1, 4, 5]

#7.2.4. Modifying Elements:

my_list = [1, 2, 3, 4, 5]

# Updating an element at a specific index

my_list[2] = 8
print("After updating element at index 2 to 8:", my_list)

After updating element at index 2 to 8: [1, 2, 8, 4, 5]

#7.2.5. List Slicing:

my_list = [1, 2, 3, 4, 5]

# Slicing the list
subset = my_list[1:4]
print("Subset from index 1 to 3:", subset)

Subset from index 1 to 3: [2, 3, 4]

#7.2.6. List Comprehension:

my_list = [1, 2, 3, 4, 5]

# Doubling each element using list comprehension
doubled_list = [x * 2 for x in my_list]  #using multiply operator for each element (x)
print("Doubled list:", doubled_list)

#8. Arrays (from array module): store collections of items of the same data type. Unlike lists, which can hold #elements of different data types, 
#arrays are homogeneous. more memory efficient for storage and manipulation of data in case of large datasets of consistent data type
#used in numerical and scientific computing and other applications where performance is crucial
#for more general-purpose use-cases, lists are often more flexible and convenient

#The array module in Python provides a way to create arrays:

from array import array

# Creating an array of integers
integer_array = array('i', [1, 2, 3, 4, 5])

# Accessing elements in the array
print(integer_array[0])  # Output: 1
print(integer_array[2])  # Output: 3

# Modifying elements in the array
integer_array[1] = 10
print(integer_array)  # Output: array('i', [1, 10, 3, 4, 5])

# Iterating through the array
for num in integer_array:
    print(num)

# Using arrays for floating-point numbers
float_array = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(float_array)  # Output: array('f', [1.1, 2.2, 3.3, 4.4, 5.5])


#9.Tuples: ordered and immutable(their values cannot be modified after creation) collection of elements created by using parentheses()
#Used when the data should remain constant throughout the program

#9.1. Creating a tuple
my_tuple = (1, 2, 3, 'four', 5.0)   #created with a mix of integer, string, and float elements

#9.2 Accessing elements by their indexes and negative indexes

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

First element: 1
Last element: 5.0

#9.3.Iterating through elements
print("Iterating through the tuple:")
for item in my_tuple:       #for loop 
    print(item)

Iterating through the tuple:
1
2
3
four
5.0    

#9.4.Tuple unpacking 
a, b, c, d, e = my_tuple
print("Unpacked variables:", a, b, c, d, e)  #assigning each element to separate variables

Unpacked variables: 1 2 3 four 5.0

#10.Sets: unordered collection of unique elements created using curly braces {} or the set() constructor

#10.1.Uniqueness: automatically eliminates duplicate elements. 
#even though the value 3 is twice, the resulting set only contains one instance of each unique element

my_set = {1, 2, 3, 3} # Results in a set {1, 2, 3}`
print (my_set)

{1, 2, 3}   

#10.2.Checking Membership: sets provide an efficient way to check whether a particular element is present 

my_set = {1, 2, 3, 3}
is_present = 4 in my_set

if is_present:
    print("True")
else:
    print("False")

False   

#10.3.Operations: like union, intersection and difference are useful in solving mathematical problems

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)         # {1, 2, 3, 4, 5, 6} uniting sets
intersection_set = set1.intersection(set2)  # {3, 4} outputting common elements
difference_set = set1 - set2          # {1, 2}  substraction of sets


#10.4.Set Comprehensions: similar to list comprehensions, sets also support set comprehensions for concise creation

squares_set = {x**2 for x in range(5)}  #outputs squares of numbers from 0 to 4
print(squares_set)

{0, 1, 4, 9, 16}

#10.5.Removing Duplicates from Lists:

my_list = [1, 2, 3, 3, 4, 5, 5]
unique_elements = set(my_list)  # {1, 2, 3, 4, 5}

#10.6. Finding Differences:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference_set = set1.difference(set2)  # {1, 2}   what numbers are missing in second set

#10.7.Removing Elements:

my_set.remove(2)  # Removes the element 2 from the set

#11.Dictionaries: unordered collection of key-value pairs created using curly braces {} or the dict() constructor.

#11.1.Creating a dictionary

my_dict = {"name": "Name", "age": 21}

#11.2.Accessing values using keys

print("Name:", my_dict["name"])  # Output: Name: Name
print("Age:", my_dict["age"])    # Output: Age: 21

#11.3. Modifying a value

my_dict["age"] = 22
print("Updated Age:", my_dict["age"])  # Output: Updated Age: 22

#11.4. Adding a new key-value pair

my_dict = {"name": "Name", "age": 21}   # do not leave this out otherwise it will show:"dictionary is not defined"!
my_dict["city"] = "City"
print("City:", my_dict["city"])  # Output: City

#11.5.Iterating through keys and values

print("Dictionary Items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#11.6.Checking if a key exists in the dictionary
    
if "nationality" in my_dict:
    print("Nationality:", my_dict["nationality"])
else:
    print("Nationality key not found in the dictionary")

#11.7.Removing a key-value pair
    
removed_value = my_dict.pop("city")
print("City:", removed_value)  # Output: Removed City: City

#11.8.Adding the nationality key-value pair

my_dict = {'name': "Name", "age": 21}
print(my_dict)
my_dict["city"] = "City"
print("city:", my_dict["city"])
my_dict["nationality"] = "Nationality" 
#print("City:", my_dict["city"])
print("nationality:", my_dict["nationality"]) 
# Checking the updated dictionary
print("Updated Dictionary:", my_dict)

{'name': 'Name', 'age': 21}
city: City
nationality: Nationality
Updated Dictionary: {'name': 'Name', 'age': 21, 'city': 'City', 'nationality': 'Nationality'}

#12. File Handling: the process of reading from and writing to files allows to interact with external files on computer's storage. 
#Python provides built-in functions and methods to perform file operations.

#12.1.Reading from a File: 
#open() function is used to open a file. The "r" argument specifies that the file is opened in read mode. 
#with statement is used for proper resource management, ensuring that the file is properly closed after use. 
#read() method reads the entire content of the file.

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#12.2.Writing to a File: use the "w" argument with the open() function. If the file does not exist, it will be created. 
#If the file already exists, its contents will be overwritten.
    
with open("output.txt", "w") as file:
    file.write("Hello, File Handling!\nThis is a new line.")   

#12.3.Appending to a File: to add content to the end of an existing file, use the "a" (append) argument with the open() function.
    
with open("output.txt", "a") as file:
    file.write("\nAppending new content.")

#12.4.Reading Lines from a File: read the content of a file line by line using a loop.   
    
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end

#13.Pip API: a package manager to install and manage third-party Python packages which allows programmatic interaction with the package manager, 
#enabling automated installation and management of Python libraries.
    
#Installing a Package using Pip API: in Python scripts utilize the subprocess module to run the Pip commands programmatically 
#Example of installing the Flask package uses the subprocess.run() function to execute the pip install command for the specified package
#The check=True parameter raises a CalledProcessError if the installation process encounters an error. 
#This approach allows to incorporate package installations into your Python scripts or automate workflows.
        
import subprocess

package_name = "flask"

#Using the Pip API to install the Flask package
try:
    subprocess.run(["pip", "install", package_name], check=True)
    print(f"Successfully installed {package_name}")
except subprocess.CalledProcessError as e:          #e is avariable used to capture exception object in case of error during execution of function subprocess()
    print(f"Error installing {package_name}: {e}")  

#subprocess.CalledProcessError is the type of exception that handles errors raised by the subprocess.run() function.
# as e assigns the exception object to the variable e. it allows to access information about the exception, such as the error message.
#in the print statement within except block {e} is used for details about the exception in the printed error message, and is helpful for debugging or logging purposes
        
#14. Git & Github: Git is a version control system, and GitHub is a platform for code sharing and collaboration that hosts repositories managed by Git
    
#Using Git in Python:   
    
#14.1.Clone a Repository:   
    
import subprocess

repo_url = "https://github.com/username/repo.git"
subprocess.run(["git", "clone", repo_url])

#14.2.Initialize a Git Repository:

subprocess.run(["git", "init"])

#git commands in terminal:
cd <dirname>  "after any change use to change dir into folder"    
git init       "initial commit"

#14.3.Add and Commit Changes:
subprocess.run(["git", "add", "file.txt"])
subprocess.run(["git", "commit", "-m", "Commit message"])

git add .    #terminal commands 
git commit -m  "some message" 

#14.4.Check Repository Status:

subprocess.run(["git", "status"])

git push origin main  #in terminal 

#14.5.Using GitHub API in Python: To interact with GitHub through Python, use the requests library or GitHub API libraries like PyGithub

import requests

username = "your_username"
token = "your_access_token"
repo_name = "new_repo"

headers = {"Authorization": f"token {token}"}
data = {"name": repo_name, "auto_init": True}

response = requests.post(f"https://api.github.com/user/repos", headers=headers, json=data)

#List Repository Contents:

repo_url = "https://api.github.com/repos/username/repo/contents"

response = requests.get(repo_url, headers=headers)

#Create a New File in Repository:

file_content = "Hello, GitHub!"

create_file_url = f"https://api.github.com/repos/username/repo/contents/new_file.txt"
data = {"message": "Create new_file.txt", "content": base64.b64encode(file_content.encode()).decode()}

response = requests.put(create_file_url, headers=headers, json=data)

#Ensure you replace placeholders like your_username, your_access_token, username, repo, etc., with actual GitHub information. 
#Also, be careful when handling tokens and sensitive information. Make sure to install necessary libraries using:

pip install requests

#15. Exceptions: allows to handle errors that may occur during the execution of code. 
#It helps to prevent program from crashing.Exceptions are raised when errors occur during the program's execution,
#they can be caught and handled using try, except, else, and finally blocks.

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Cannot divide by zero!")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
else:
    # This block is executed if no exceptions occur in the try block
    print("No errors occurred.")
finally:
    # This block is always executed, whether an exception occurred or not
    print("Finally block executed.")

#16. Debugging: identifying and fixing errors in the code
    
    def divide_numbers(a, b):
    result = a / b
    return result
# Assume we want to find the result of dividing 10 by 0
numerator = 10
denominator = 0
# places a breakpoint in the next line
# allows to inspect variables and step through the code
# using a debugger, like pdb (Python Debugger)

import pdb; pdb.set_trace()

result = divide_numbers(numerator, denominator)

print(f"The result is: {result}")

#17. Testing Modules: writing and running tests are crucial in software development for ensuring that code functions as expected and to catch any potential errors or bugs

#17.1.Writing Tests: to check the correctness of functions or modules of code by each test focusing on a specific functionality or scenario.
#Testing modules, such as unittest, pytest, or others, provide structures for organizing and running tests.

# Assertions: in the test case used to check if the actual output matches the expected result. If the assertion fails, the testing framework reports an error.

def test_addition():
    assert add(2, 3) == 5

#17.2.Running Tests: testing modules provide mechanisms to discover and execute tests.run tests from the command line or within an integrated development environment (IDE).
#A testing framework executes all test cases and reports any failures.

pytest test_my_module.py   #it is in bash environment

#17.3.Test Fixtures: allow to set up and tear down resources needed for tests ensuring a clean and consistent environment for each test

import pytest

@pytest.fixture
def setup_data():
    return data        # Set up test data or resources

def test_something_with_setup(setup_data):
    assert something_with_data(setup_data) == expected_result  # Test using the setup_data fixture

#Test Discovery: often included automatically making it easy to locate and run all tests in a project and helps maintain a omprehensive suite of tests as codebase evolves  
#by incorporating testing modules into your development workflow, we can systematically verify that ode behaves correctly under various conditions, 
#reducing the likelihood of introducing bugs and ensuring the reliability of your software. The example uses the pytest framework, but other testing frameworks 

#18. Agile & Scrum: Project management methodologies for software development
    
# Product Backlog - List of features to be implemented
product_backlog = ["Feature A", "Feature B", "Feature C"]

# Sprint Planning - Select features for the sprint
sprint_backlog = ["Feature A", "Feature B"]

# Sprint - Implement selected features in a time-boxed iteration
for feature in sprint_backlog:
    # Developer works on the feature
    print(f"Working on {feature}")

    # Code review
    print(f"Code review for {feature}")

    # Testing
    print(f"Testing for {feature}")

# Sprint Review - Demonstrate completed features

completed_features = ["Feature A"]
print("Sprint Review:")
for feature in completed_features:
    print(f"Completed: {feature}")

# Sprint Retrospective - Reflect on the sprint and plan improvements
print("Sprint Retrospective:")
print("What went well?")
print("What could be improved?")

#19. Program Flow: Control of the order in which statements are executed

# Conditional Statement (if-else)
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Loop (for loop)
print("Printing numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop (while loop)
print("Printing numbers from 5 to 1:")
counter = 5
while counter >= 1:
    print(counter)
    counter -= 1

#20.Python Database & API: Interacting with databases and web APIs in Python
 
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (list of dictionaries)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# API endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API endpoint to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

#21.Lambda (Anonymous Functions): short, concise functions using lambda keyword for simple operations where a full function definition is not necessary. 
 
#Example: lambda function square, which takes one argument x and returns its square, is defined to calculate the square of a given number 
#This provides a more compact alternative to defining a traditional function.  

square = lambda x: x**2
result = square(4)  # Result: 16

#22.Regular Expressions (Regex):powerful tools for complex pattern matching and manipulation of strings. 
#The re module in Python provides support for working with regular expressions. 
#Example: the re.search() function is used to find the first occurrence of one or more digits in a string.

import re
result = re.search(r'\d+', 'abc123def').group()

#r'\d+': regular expression pattern searches for one or more digits (\d) in a string.
#'abc123def': input string on which the search operation is performed.
#re.search(): searches for the first occurrence of the pattern in the string.
#result is the string '123', because it is the first sequence of digits found in the input string. 









   




