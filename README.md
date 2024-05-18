# Object Oriented Programming (OOP) in Python

01. Classes
02. Methods-Functions
03. Objects
04. Constructors
05. Inheritance
06. Encapsulation
07. Polymorphism
08. Decorators
09. Method Overloading
10. Method Overriding


### 01. Classes

In Python Classes are template/blueprints for creating an object, Classes contains attributes and methods which can be accessed through an object. 
In Python, classes are defined using the “Class” keyword

```
class myClass():
```

### 02. Methods-Functions

- Inside classes, you can define attributes and methods that are part of the class

```
def method1 (self):
   print("OOP")
def method2 (self, something): 
   print ("Program-Method"+ something)
```
Here we have defined method1 that prints “OOP”
Another method we have defined is method2 that prints “Program-Method”+ something. something is the variable supplied by the calling method

- Everything in a class is indented, just like the code in the method, loop, if statement, etc. Anything not indented is not in the class
```
class myClass():
    def method1 (self):
        print("OOP")
    def method2 (self, something): 
        print ("Program-Method" + something)
```
- [Note]
    - “self”
        - The self-argument refers to the object itself. Hence the use of the word self. So inside this method, self will refer to the specific instance of this object that’s being operated on.
        - Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python. It is part of the Python syntax to access members of objects

- Types of methods-
    * Instance Method
    * Class Method
    * Static Method
        
        * We have one more method called the 'magic method'

### 03. Objects

- How to construct an object of the class?
- here 'my_turtle' is an object constructing the class 'Turtle'
```
my_turtle = Turtle()
```

- How to call a method in a class?
```
my_turtle.color("red")
```

### 04. Constructors

Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

```
def __init__(self):
    # body of the constructor
```

### 05. Inheritance

In Inheritance, one class can derive the properties of another class.
ex- Child Inheriting features from his Father

``` # Define the parent class (Father)
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Define the child class (Child), inheriting from Father
class Child(Father):
    def __init__(self, name, age, hobby):
        # Call the __init__ method of the parent class using super()
        super().__init__(name, age)
        self.hobby = hobby

    # Method specific to the Child class
    def display_hobby(self):
        print("Hobby:", self.hobby)

# Create an instance of the child class
child1 = Child("John", 10, "Playing football")

# Accessing properties and methods of the parent class
child1.display_info()  # This will print both name and age
# Accessing property of the child class
child1.display_hobby()  # This will print the hobby
```


#### 06. Encapsulation

Encapsulation involves the bundling of data members and functions inside a single class. Bundling similar data members and functions inside a class also helps in data hiding. Encapsulation also ensures that objects are self-sufficient functioning pieces and can work independently.

```
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

    def update_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be a positive number.")

# Create an instance of the Person class
person = Person("Alice", 30)

# Accessing public method to display information
person.display_info()

# Attempting to access private attributes directly (will result in an error)
# print(person.__name)

# Accessing private attributes indirectly using a public method
person.update_age(35)

# Displaying updated information
person.display_info()

```

### 07. Polymorphism

The literal meaning of polymorphism is the condition of occurrence in different forms.
Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. Also, it is possible to modify a method in a child class that it has inherited from the parent class.

```
class Animal:
    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    return animal.speak()

# Create instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Demonstrate polymorphism
print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
print("Bird says:", animal_sound(bird))

```


### 08. Decorators

A decorator takes in a function, adds some functionality and returns it.
Decorators are used to add functionality to an existing code.

This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

```
import time

# Decorator function to log the time taken by a function
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

# Example function that we want to decorate
@timeit
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Call the decorated function
result = calculate_sum(1000000)
print("Result:", result)
```

### 09. Method Overloading

Two methods cannot have the same name in Python. For that, we use Method Overloading it does not allow different names for the method, but is a feature that allows the same operator to have different meanings.

Overloading is the ability of a function or an operator to behave in different ways based on the parameters that are passed to the function, or the operands that the operator acts on.

In Python, you can create a method that can be called in different ways. So, you can have a method that has zero, one or more number of parameters. Depending on the method definition, we can call it with zero, one or more arguments.
```
class Shape:
    def area(self):
        return 0  # Default implementation for shapes without area

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius ** 2

# Create instances of different shapes
rectangle = Rectangle()
circle = Circle()

# Calculate the area of a rectangle
print("Area of rectangle (5x3):", rectangle.area(5, 3))

# Calculate the area of a circle
print("Area of circle (radius 4):", circle.area(4))
```

### 10. Method Overriding
Method overriding in Python allows a subclass to provide its own implementation of a method that is already defined in its superclass, ensuring that when the method is called on an instance of the subclass, the subclass's implementation is executed instead of the superclass's.
```
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the overridden methods
dog.sound()  # Output: Dog barks
cat.sound()  # Output: Cat meows

```
