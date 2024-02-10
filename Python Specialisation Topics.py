#Python Specialisation Author: Gina Rubik

#19. Jira & Tableau: project management and data visualization tool

import requests   #use of request library by importing to make an HTTP GET request to a Jira API endpoint

#91.1. Define Jira API endpoint and necessary credentials(username and API token) for authentication:

jira_url = "https://your-jira-instance/rest/api/2/issue/ISSUE-123"
jira_user = "your_username"
jira_token = "your_api_token"

# Fetching data from Jira using requests.get() to send HTTP request to specified Jira API endpoint, including necessary authorization headers:

headers = {"Authorization": f"Basic {jira_user}:{jira_token}"}
response = requests.get(jira_url, headers=headers)

# Displaying Jira issue details checks if the HTTP response status code is 200 (OK). 
#If successful, it extracts and prints relevant information about the Jira issue: key and summary
#If the request is unsuccessful, it prints an error message with the received status code

if response.status_code == 200:
    issue_data = response.json()
    print(f"Jira Issue Key: {issue_data['key']}")
    print(f"Summary: {issue_data['fields']['summary']}")
else:
    print(f"Failed to fetch data from Jira. Status Code: {response.status_code}")

#19.2.Use of the TableauServerConnection class from the tableau_api_lib library to connect to a Tableau Server, fetch a list of projects, and display their names.  

from tableau_api_lib import TableauServerConnection  #imports TableauServerConnection class from tableau_api_lib library designed for interacting with Tableau Server

# Tableau Server connection details: define the details to connect to the Tableau Server, including the server URL, user credentials (username and password) and the site

server = "https://your-tableau-server"
username = "your_username"
password = "your_password"
site = "your_site"

# Connecting to Tableau Server: instance of the TableauServerConnection class with specified details and sign_in() method called to establish a connection to the Tableau Server

connection = TableauServerConnection(server, username, password, site)
connection.sign_in()

# Fetching a list of Tableau projects: query_projects() method to retrieve a list of Tableau projects associated with the connected server

projects = connection.query_projects()

# Displaying Tableau projects: loop that iterates through the list of projects and prints their names.

for project in projects:
    print(f"Tableau Project: {project.name}")

# Signing out from Tableau Server: sign_out() method is called to disconnect and log out from the Tableau Server
    
connection.sign_out()


#20.OOP(Object-Oriented Programming): programming paradigm with 3 principles organising code into objects which can have attributes (data) and methods (functions)

#20.1.Class: blueprint for creating objects and defines a data structure and methods to operate on that data

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

#20.2.Object: an instance of a class representing a real-world entity and has attributes and methods
        
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info()  # Output: Toyota Camry
car2.display_info()  # Output: Honda Civic

#20.3.Encapsulation: refers to bundling data (attributes) and methods that operate on the data within a single unit (class), helps hiding internal details of object 
#and exposing only what is necessary
       
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute
        self._mileage = 0    # Protected attribute

    def display_info(self):
        print(f"{self._brand} {self._model}, Mileage: {self._mileage} miles")

    def drive(self, miles):
        self._mileage += miles

    # Protected method
    def _maintenance_alert(self):
        if self._mileage >= 10000:
            print("Maintenance Alert: Schedule a service!")

# Example usage
car = Car("Toyota", "Camry")
car.display_info()  # Output: Toyota Camry, Mileage: 0 miles

car.drive(5000)
car.display_info()  # Output: Toyota Camry, Mileage: 5000 miles

# Attempt to access protected attribute directly (not recommended)
# Note: Conventionally, attributes/methods starting with a single underscore are considered protected
print(car._mileage)  # Output: 5000

# Attempt to call a protected method (not recommended)
car._maintenance_alert()  # Output: Maintenance Alert: Schedule a service!

#20.4.Inheritance: allows a class (subclass/derived class) to inherit attributes and methods from another class (superclass/base class).
#promotes code reusability and establishes an "is-a" relationship between classes

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
electric_car.display_info()  # Output: Tesla Model S

#20.5.Polymorphism: allows objects of different types to be treated as objects of a common type which can be achieved through method overloading or method overriding

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sounds(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sounds(dog)  # Output: Woof!
animal_sounds(cat)  # Output: Meow!

#21.Decorators: modifying or extending the behavior of functions or methods, powerful feature in Python, enabling the modification of functions or methods without 
#altering original code and commonly used for aspects like logging, timing, and access control.

#21.1.Decorator Definition: my_decorator function is taking a function (func) as an argument, defines a new function (wrapper) that wraps around the original function 
#and returns the wrapper function
        
def my_decorator(func):
    def wrapper():        #wrapper function within the decorator is responsible for adding behavior before and after calling the original function
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

#21.2.Decorating a Function: @my_decorator syntax is used to apply my_decorator to say_hello function, equivalent to say_hello = my_decorator(say_hello).

@my_decorator
def say_hello():   #say_hello is called, invoking the wrapper function due to the decorator resulting in additional actions before and after the original function call
    print("Hello!")

#21.3. Output: demonstrates augmented behavior introduced by the decorator, showcasing additional actions surrounding the execution of the say_hello function
    
vbnet: 
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

#22.Collections: specialized container data types with efficient solutions for various data manipulation tasks, providing specialized features beyond basic data structures
    
from collections import Counter  #imports the Counter class from the collections module

# Sample list of elements sample is defined with repeated occurrences of certain values:
my_list = [1, 2, 3, 1, 2, 3, 4, 1, 2, 1]

# Using Counter to count occurrences
element_counts = Counter(my_list) #to create a dictionary-like object where keys represent unique elements from the list and values represent the count of each element

# Displaying the counts
for element, count in element_counts.items():
    print(f"Element {element} occurs {count} times.") # resulting element_counts object can be utilized to quickly retrieve the count of specific elements in the original list

Counter({1: 4, 2: 3, 3: 2, 4: 1}) #indicates that the element 1 appears 4 times, 2 appears 3 times, 3 appears 2 times, and 4 appears 1 time in the original list

#23.Iterators: objects that can be iterated (looped) over allowing sequential access to elements to create them from iterable objects using the iter() function
#fundamental to Python's iteration protocol, enabling efficient and memory-friendly traversal of data structures. 
#used implicitly in for loops, comprehensions, and other constructs that involve iteration

#23.1.Creating an iterable:
my_iterable = [1, 2, 3]
# Creating an iterator from the iterable
my_iterator = iter(my_iterable)

#23.2.Accessing elements using the my_iterator() function:
element1 = next(my_iterator)            
                                     #next() function is used to retrieve each element from the iterator sequentially.
element2 = next(my_iterator)            
element3 = next(my_iterator)

print(element1, element2, element3)  #my_iterable is a list, and my_iterator is an iterator created from that list

#Output: 1 2 3 once all elements have been retrieved, if you try to call next(my_iterator) again, it will raise a StopIteration exception, signaling the end of the iteration

#24.Generators: a type of iterable, unlike lists or tuples, they generate values on-the-fly rather than storing them in memory
#memory-efficient because they generate values on-demand, making them suitable for scenarios where dealing with large datasets or continuous streams of data 


def my_generator():       
    yield 1              #using the yield keyword to iterate over generator object to produce a series of values one at a time 
    yield 2              #yield statement allows the generator function to "pause" and "resume" its execution state, remembering the last yielded value
    yield 3

gen = my_generator()     #my_generator is a generator function, when you call it, doesn't execute the code immediately, instead, returns a generator object

for value in gen:
    print(value)

1
2
3

#25.Itertools Library: A library providing building blocks for iterators
    
from itertools import combinations


#26.Troubleshooting: identifying and fixing issues in the code or environment

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    # Intentional mistake: using 'sum' as a variable name
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Intentional mistake: passing the wrong variable to the function
result = calculate_average(numbers_list)

# Print the result
print(f"The average is: {result}")

#Data Structures

#27.Stacks & Queues: 
#data structures with specific rules for adding and removing elements essential for managing collections 
#Queues are commonly used in task scheduling, while stacks find applications in parsing expressions or managing function calls 
#Deques provide a versatile alternative with fast operations on both ends

#Queues (from queue module): provides FIFO (First In, First Out) order for elements.

import queue; my_queue = queue.Queue() #elements are added at the rear (enqueue) and removed from the front (dequeue) and queue.Queue() creates a queue object

#Stacks: Provides LIFO (Last In, First Out) order for elements. Can be implemented using lists

#Double-ended queue: allows fast appends and pops from both ends, provides flexibility in adding or removing elements from either end efficiently

from collections import deque; my_deque = deque([1, 2, 3])

stack = [1, 2, 3]   #elements are added to the top (push) and removed from the top (pop) 
stack.append(4)     #stack is a list acting as a stack, and append(4) adds the element 4 to the top of the stack

#28.Hash Tables & Hashing: 
#data structure that maps keys to values for efficient retrieval. Hash tables are data structures that implement an associative array 
#abstract data type using a hash function to map keys to indices, allowing for efficient retrieval of values based on their keys
#Hashing enables efficient data retrieval, making it suitable for scenarios where quick access to values based on keys is crucial. 
#Python dictionaries, sets, and other hash-based data structures leverage this concept for efficient data storage and retrieval.

my_dict = {"name": "Name", "age": 21} #my_dict is a dictionary, type of hash table, keys ("name" and "age") are hashed to generate indices for quick access 
                                       #to their values ("Name" and 21).

#29.Recursion: 
#programming concept where function calls itself during its execution,useful for solving complex problems by breaking them down into smaller more manageable 
#instances; to be used judiciously to avoid infinite loops and proper termination conditions (base cases) are crucial for the recursive function to converge

def factorial(n):  #factorial function calculates the factorial of a number n,base case (if n == 0) is defined, in the recursive case the function calls itself with 
                   #smaller argument (n-1) which...
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  #...continues until the base case is reached, the results are combined to compute the final factorial

#30.Time & Space Complexity: measures of algorithm efficiency
    
def fibonacci(n):            #Time and Space Complexity: O(n) 
    
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
n = 10
result = fibonacci(n)

print(f"The first {n} Fibonacci numbers are: {result}")

#31.Algorithms & Sorting: step-by-step procedures for solving problems and arranging elements

def bubble_sort(arr):     #sorts list using Bubble Sort algorithm: simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
                          #and swaps them if they are in the wrong orde
                          #Time Complexity: O(n^2) in the worst case, where 'n' is the number of elements in the list
                          #Space Complexity: O(1), because the algorithm doesn't use additional memory proportional to the input size
    
    n = len(arr)

    for i in range(n):             #outer loop that represents each pass through the list
                                   # last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):  #inner loop compares adjacent elements and swaps them if they are in the wrong order
                                  
            if arr[j] > arr[j+1]:  #swap if the element found is greater than the next element
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original List: {my_list}")

bubble_sort(my_list)                #bubble_sort function takes a list as input and sorts it in ascending order using the Bubble Sort algorithm

print(f"Sorted List: {my_list}")

#32.Largest Number in Arrays:

def find_largest_number(arr):         #function that takes array as input and iterates through it to find the largest number, 
                                      #Time Complexity: O(n) where 'n' is the number of elements in the array.
                                      #Space Complexity: O(1), because the algorithm uses a constant amount of extra space regardless of the input size
    
    if not arr:
        return None
    

# Example usage
my_array = [12, 45, 89, 67, 34, 102, 56]
largest_number = find_largest_number(my_array)  #function iterates through the array, updating max_number whenever a larger number is encountered

print(f"The largest number in the array is: {largest_number}")

#33.Linked Lists: a linear data structure where elements are linked using pointers

class Node:                      #Node class represents a node in the linked list, with a data field and a next field pointing to the next node

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:                 #LinkedList class has a head field pointing to the first node
    
    def __init__(self):
        self.head = None

    def append(self, data):       #append method adds a new node with the given data at the end of the linked list
        
        new_node = Node(data)     #append a new node with the given data at the end of the linked list
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):              #display method prints the elements of the linked list
        
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    
    linked_list.display()

#Output: 10 -> 20 -> 30 -> None                 

#34.Binary Trees: a tree data structure where each node has at most two children referred to as the left child and the right child
#used in various applications:expression trees, file systems, database indexing. They provide efficient way to represent hierarchical structures 
#and facilitate operations such as searching, insertion, and deletion of elements
    
class TreeNode:     #represents a node in the binary tree. Each node has a value and references to its left and right children
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Example binary tree: defines a simple binary tree with nodes containing integer values
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Function to perform in-order traversal of the binary tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)        #printing the values of nodes in ascending order

print("In-order Traversal of Binary Tree:")  #in-order traversal of the binary tree is called, and the result is printed 
inorder_traversal(root)

    
#35. Graphs: a collection of nodes connected by edges,fundamental in computer science having various applications: social network analysis, routing algorithms, 
#and dependency resolution, providing a versatile way to model and analyze relationships between different entities

from collections import defaultdict

class Graph:                           #represents a graph using an adjacency list. Nodes are stored as keys in a dictionary, 
                                       #and the corresponding values are lists of neighboring nodes.
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

# Example graph: defines a simple directed graph and adds edges between nodes using the add_edge method.
my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)

# Function to perform depth-first traversal of the graph: defines a simple graph using an adjacency list representation performing depth-first traversal starting from node 1

def dfs(graph, node, visited):              #performs a depth-first traversal of the graph starting from a specified node
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("\nDepth-First Traversal of Graph:")  #prints the visited nodes in the traversal order
dfs(my_graph.graph, 1, set())


