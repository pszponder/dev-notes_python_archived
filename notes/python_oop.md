# Python OOP

Everything in Python is an Object

**Object-oriented programming** (OOP) is a method of structuring a program by bundling related properties and behaviors into individual **objects**

> OOP allows us to create our own Python types, with their own attributes and methods.

## Quick Summary

```python
###############################
# Define a class called MyClass
###############################
class MyClass:
    # This is the constructor method
    def __init__(self, value):
        self.instance_property = value

    class_property = 10

    @classmethod
    def class_method(cls):
        print("This is a class method")

    def instance_method(self):
        print("This is an instance method")


#######################
# Instantiate the Class
#######################
my_object = MyClass(20)

###################
# Access Properties
###################

# Access Class Property
print(MyClass.class_property)  # Output: 10

# Access Instance Property
print(my_object.instance_property)  # Output: 20

################
# Access Methods
################

# Access Class Method
MyClass.class_method()  # Output: This is a class method

# Access Instance Method
my_object.instance_method()  # Output: This is an instance method
```

## Defining a Class in Python

Use the `class` keyword to define a new Python class.

```python
# Define a new class in Python
class MyClass:
    # class code here...
    pass
```

### Class Naming Convention

Class naming follows the PascalCase naming convention

### Defining a class constructor using `__init__()`

The `__init__()` method is responsible for setting the initial **state** of the object by assigning the values of the object's properties when it is instantiated from the class.

How to define a class constructor in Python

1. Use the `__init__()` `dunder method` (a `dunder method` is a special reserved class method which ends with double underscores)
2. Pass the `self` as the 1st parameter into the `__init__()` method

Ex. `__init__(self, param1, param2, param3, ...)`

**NOTE:** `__init__()` is _Optional_

- If you don't have any parameters to pass into a class, you don't need a class constructor (don't need to include `__init__()` in the class definition)

**NOTE:** `self` parameter in `__init__()`

- You can give `.__init__()` any number of parameters, but the first parameter will always be a [variable](https://realpython.com/python-variables/) called `self`.
- When a new class instance is created, the instance is automatically passed to the `self` parameter in `.__init__()` so that new **attributes** can be defined on the object.
- Think of `self` as the equivalent to the `this` keyword in other languages like JavaScript or C#

```python
# Define the Dragon Class
class Dragon:
    # Create a constructor method using __init__()
    #  which accepts a name and age argument
    #  when instantiating the class
    def __init__(self, name, age):
        # The passed in arguments of name and age will be
        # assigned to the instance's name and age attributes
        self.name = name
        self.age = age
```

In the above code, in the body of `.__init__()`, there are two statements using the `self` variable:

1. `self.name = name` creates an attribute called `name` and assigns it to the value of the `name` parameter
2. `self.age = age` creates an attribute called `age` and assigns to it the value of the `age` parameter

**NOTE:** Can pass default values into constructor method (`__init__()`)

```python
# NOTE: You will recieve errors if you try to instantiate
#  the class with an age <= 18
class PlayerCharacter:
    # Constructor Method
    # Set default values if they're not passed in upon initialization
    def __init__(self, name="anonymouse", age=0):
        if (age > 18):
            self.name = name
            self.age = age

    # Instance method
    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f"my name is {self.name}")

# Create multiple instances of the class
player1 = PlayerCharacter("Bob", 44)
player2 = PlayerCharacter("Sally", 22)

print(player1.name)  # Bob
print(player1.age)   # 44
print(player1.run()) # Prints 'run' to console and returns 'done'

print(player2.name)  # Sally
print(player2.age)   # 22
print(player2.run()) # Prints 'run' to console and returns 'done'
```

### Instance & Class Attributes

Attributes are synonymous with properties.

`Instance Attributes`

- Attributes created in `.__init__()` are called **instance attributes**.
- An instance attribute’s value is specific to a particular instance of the class.

`Class Attributes`

- Attributes that have the same value for all class instances are called **class attributes**.
- You define a `class attribute` by assigning a value to a variable name outside of `.__init__()`
- Class attributes are defined directly beneath the first line of the class name.
- `Class Attributes` must always be assigned an initial value
- When an instance of the class is created, `class attributes` are automatically created and assigned to their initial values.

```python
# Define the Dragon Class
class Dragon:
    # Class attribute (Same for each instance)
    has_magic = True
    species = "Drago familiaris"

    def __init__(self, name, age):
        # Instance Attributes (unique to each instance)
        self.name = name
        self.age = age
```

`Class Attributes` vs `Instance Attributes`

- Use `class attributes` to define properties that should have the same value for every class instance.
- Use `instance attributes` for properties that vary from one instance to another.

**CAUTION:** Custom objects are mutable by default

- This means that once you can access either a `class attribute` or an `instance attribute` from a class / instance and change the attribute value using dot notation.
- To make a `protected` or `private` attribute, prepend the attributes with either a single or double underscore (see section on [[python_oop#Encapsulation|encapsulation]])

### Instance Methods

**Instance methods** are functions that are defined inside a class and can only be called from an instance of that class.

- Just like `.__init__()`, an instance method’s first parameter is always `self`.

```python
# Define the Dragon Class
class Dragon:
    has_magic = True
    species = "Drago familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method 1
    # Return a string displaying the name and age of the dragon
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance method 2
    # Return a string containing name and sound the dragon makes
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

### Class & Static Methods

Both `class methods` and `attribute methods` are methods which belong to the class instead of the method.

Declaring a `Class Method`

1. Add the `@classmethod` decorator above the method definition
2. Pass in `cls` instead of `self` as the first parameter of the method

Declaring `Static Method`

1. Add the `@staticmethod` decorator above the method definition
2. **_Don't_** add `self` or `cls` as the first parameter of the method

Both `class method` and `static methods` can be invoked directly from the Class definition itself instead of needing to invoke it from the instance.

`Class Methods` vs `Static Methods`

- `Class Methods` have access to `cls` which allows them to reference a class or instance state (attributes / methods).
- `Static Methods` do not have access to `cls`

```python
class Dragon:
    has_magic = True
    species = "Drago familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a class method
    # Note the convention of passing in "cls" instead of "self"
    @classmethod
    def eat(cls, sound):
        return f"{sound}, {sound}, {sound}"

    # Define a static method
    # don't have access to "cls" in this case
    @staticmethod
    def fight():
        return "preparing to fight..."


# Instantiate two methods
dragon1 = Dragon("Alduin", 10000)
dragon2 = Dragon("Smaug", 1000)

# Invoke the eat method on the class instances
print(dragon1.eat("Nom"))  # Nom, Nom, Nom
print(dragon2.eat("Crunch"))  # Crunch, Crunch, Crunch

# Since eat is a class method, we can call it directly from the class
print(Dragon.eat("Munch"))  # Munch, Munch, Munch
```

### Public, Protected, and Private Access Modifiers

`Access modifiers` are ways of defining what may access a specific attribute or method.

Defining an attribute/method as `public`, `protected`, or `private`

- In Python, to change the accessibility of an attribute or method, use underscores:
- An attribute / method **NOT** prefixed with any underscores is considered `public`
- An attribute / method prefixed with a single underscore (`_`) is considered `protected`
- An attribute / method prefixed with a double underscore (`__`) is considered `private`

**CAUTION:** Convention for defining attribute / method as `private`

- Since `dunder methods` also start with double underscores (`__`), it is actually convention in Python to define `private` attributes / methods using a single underscore (`_`).
- **Note** that this is only convention since technically, a single underscore denotes a `protected` attribute / method and so you can actually still access these outside of the class definition (so not truly `private`)

`protected` vs `private` in Python

- The main difference between `protected` and `private` attributes / methods is in how they are accessed from outside of the class.

`Protected`:

- Denoted by a single underscore (`_`) before the attribute / method name.
- However, this is just a convention, and the attribute / method can still be accessed from outside the class if the user knows the attribute name.
- Protected attributes / methods are intended to signal to the developer that they should not access or modify the attribute / method from outside the class, but the interpreter does not enforce this.

`Private`:

- Denoted by a double underscore (`__`) before the attribute / method name.
- The name of the attribute / method is "mangled" by Python interpreter to avoid naming collisions with attributes / methods defined in subclasses or other modules.
- Private attributes / methods are intended to be accessed and modified only within the class in which they are defined.
- They are not visible to the outside world, even if the user knows the attribute / method name.

```python
# Define protected attribute / method w/ single leading underscore
# Define private attribute / method w/ double leading underscore

class MyClass:
    def __init__(self):
        # Can be accessed and modified from outside the class
        self.public_attribute = 1  # public attribute

        # Can be accessed and modified
        #  from within the class and its subclasses
        # NOTE: This is just convention,
        #  can still access from outside
        self._protected_attribute = 2  # protected attribute

        # Can only be accessed and modified
        #  from within the class itself
        # NOTE: Python convention is NOT to use double underscores
        #  for private attributes / methods since "dunder methods"
        #  also start with double underscores
        self.__private_attribute = 3  # private attribute

    # Can be called from outside the class
    def public_method(self):
        # public method
        self.public_attribute += 1
        self._protected_attribute += 1
        self.__private_attribute += 1

    # Can only be accessed and called from within class itself
    #  and its subclasses
    # NOTE: This is just convention,
    #  can still access from outside
    def _protected_method(self):
        # protected method
        self.public_attribute += 1
        self._protected_attribute += 1
        self.__private_attribute += 1

    # Can only be accessed and called from within the class itself
    # NOTE: Python convention is NOT to use double underscores
    #  for private attributes / methods since "dunder methods"
    #  also start with double underscores
    def __private_method(self):
        # private method
        self.public_attribute += 1
        self._protected_attribute += 1
        self.__private_attribute += 1

    # A public method that can be called from outside the class
    #  and returns the value of the private attribute
    # Common examples are getters and setters
    def get_private_attribute(self):
        return self.__private_attribute


# Instantiate the class
my_obj = MyClass()

# Accessing public attribute from outside the class
print(my_obj.public_attribute)  # Output: 1

# Calling public method from outside the class
my_obj.public_method()
print(my_obj.public_attribute)  # Output: 2

# Accessing protected attribute from outside the class
print(my_obj._protected_attribute)  # Output: 3

# Calling protected method from outside the class
my_obj._protected_method()
print(my_obj._protected_attribute)  # Output: 4

# Accessing private attribute from within the class
print(my_obj.get_private_attribute())  # Output: 5

# Calling private method from within the class
# This uses the "name mangling" technique
my_obj._MyClass__private_method()
print(my_obj.get_private_attribute())  # Output: 6
```

```python
# Define a protected attribute with a single leading underscore
# Define a private attribute with a double leading underscore


class MyClass:
    public_class_attr = "public class attribute"
    _protected_class_attr = "protected class attribute"
    __private_class_attr = "private class attribute"

    def __init__(self):
        self.public_instance_attr = "public instance attribute"
        self._protected_instance_attr = "protected instance attribute"
        self.__private_instance_attr = "private instance attribute"


obj = MyClass()

# Accessing public attributes
print(obj.public_class_attr)  # "public class attribute"
print(obj.public_instance_attr)  # "public class attribute"

# Change public attributes
obj.public_class_attr = "updated public class attribute"
print(obj.public_class_attr)  # updated public class attribute
obj.public_instance_attr = "updated public instance attribute"
print(obj.public_instance_attr)  # updated public instance attribute

# Accessing protected attributes
print(obj._protected_class_attr)  # protected class attribute
print(obj._protected_instance_attr)  # protected instance attribute

# Change protected Attributes
obj._protected_class_attr = "updated protected class attribute"
print(obj._protected_class_attr)  # updated protected class attribute
obj._protected_instance_attr = "updated protected instance attribute"
print(obj._protected_instance_attr)  # updated protected instance attribute

# Accessing private attributes (can't do this, nor can you update private attributes)
print(
    obj.__private_class_attr
)  # AttributeError: 'MyClass' object has no attribute '__private_class_attr'...
print(
    obj.__private_instance_attr
)  # AttributeError: 'MyClass' object has no attribute '__private_instance_attr'...
```

## Instantiate an Object in Python

To instantiate a class, simply add a pair of parenthesis with any relevant constructor arguments into the class (just like invoking a function)

```python
# Define the Dragon Class
class Dragon:
    has_magic = True
    species = "Drago familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# Instantiate the Dragon Class
dragon = Dragon("Smaug", 5000)

# Print the Class Attributes from the Instance
print(dragon.has_magic)  # True
print(dragon.species)  # Drago familiaris

# Can also call class attributes directly from the class
print(Dragon.has_magic)  # True
print(Dragon.species)  # Drago familiaris

# Print the Instance Attributes
print(dragon.name)  # "Smaug"
print(dragon.age)  # 5000

# Invoke the instance methods of the dragon instance
print(dragon)  # (This invokes __str__) Smaug is 5000 years old
print(dragon.speak("ROAR!"))  # Smaug says ROAR!
```

## Dunder Methods

`Dunder methods` are reserved methods derived from the base object class in Python.

`Dunder methods` are defined by two sets of leading and trailing underscores wrapping the `dunder method` name.

You can overwrite the `dunder methods` of a custom python class in order to implement custom functionality

[List of Python Dunder Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)

### Constructor method with `__init__()`

[[python_oop#Defining a class constructor using `__init__()`|__init__()]]

### Representing class object as a string w/ the `__str__()` method

Use the `__str__()` `dunder` method to return a description of the class as a string when the `print()` or `str()` are invoked on the class instance. (A `dunder` method is a special reserved class method which ends with double underscores)

The `__str__()` method is called when the following functions are invoked on the object and return a string:

- `print()`
- `str()`

```python
# Define the Dragon Class
class Dragon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Invoke this method when printing the instance of this class
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

dragon = Dragon("Smaug", 5000)

# Invoke the __str__() method
print(dragon) # Smaug is 5000 years old
```

## 4 Pillars of OOP

### Encapsulation

`Encapsulation` is the process of hiding the implementation details of an object from the outside world.

In the case of OOP, the class itself is an encapsulation of attributes and methods. So all logic required for a particular class is encapsulated by that class.

### Abstraction

`Abstraction` is the process of reducing complexity by hiding unnecessary details.

In Python Classes, think of any method as abstracting away (hiding) the logic for a specific task.

Using `access modifiers` is another way of abstraction (controlling who has access to these attributes)

### Inheritance

`Inheritance` is a concept in object-oriented programming in which a class derives (or inherits) attributes and behaviors from another class without needing to implement them again.

Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.

Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.

How to inherit from a class in Python?

- To inherit from a class in python, pass the name of the parent class into the child class in the class definition (in parenthesis)

Child / Sub-Classes

- A class which inherits from a parent class is considered a child / sub class of that parent class

```python
# Define a User class
# This will be the parent class of the Wizard and Archer class
class User:
    def sign_in(self):
        print("logged in")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f"Shot an arrow: arrows left - {self.num_arrows}")


# Instantiate the child classes
# Notice that although neither of the child classes had the "sign_in" method in their class definitions
#  they can still use these methods as "sign_in" is inherited from the User parent class

## Instantiate a wizard
wizard = Wizard("Merlin", 50)
wizard.sign_in()  # "logged in"
wizard.attack()  # attacking with power of 50

## Instantiate an archer
archer = Archer("Robin", 100)
archer.sign_in()  # "logged in"
archer.attack()  # Shot an arrow: arrows left - 99
```

```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("")

# Child Class of Animal Class
# Pass the parent class into the class definition of the child class
class Dog(Animal):
    # Overwrite the speak method inherited from the parent class
    # This is polymorphism
    def speak(self):
        print("Woof!")

# Child Class of Animal Class
# Pass the parent class into the class definition of the child class
class Cat(Animal):
    # Overwrite the speak method inherited from the parent class
    # This is polymorphism
    def speak(self):
        print("Meow!")

dog = Dog("Rover")
cat = Cat("Whiskers")
dog.speak()   # output: Woof!
cat.speak()   # output: Meow!
```

#### Inheriting w/ `super()`

At a high level `super()` gives you access to methods in a superclass (parent class) from the child / subclass that inherits from it.

What does `super()` do?

- `super()` alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.

**CAUTION:** Don't pass `self` into methods invoked on `super()`

- When using `super()`, any method that is invoked on `super()` should not have the `self` keyword passed into it, this is already handled by `super()` under the hood.

Using the `super()` method to access parent attributes

- To access attributes from a parent class using the `super()` method, inside the subclass' `__init__()` method, make a call to the following:
- `super().__init__(param1, param2, param3, ...)`
- This will invoke the superclass' `__init__()` method

```python
# Parent class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        # Invoke the super() method to instantiate the
        #  constructor method of the parent class
        # Pass in length as both "length" and "width" attributes
        # Since the "Square" class inherits from "Rectangle",
        #  it also has access to the "area" & "perimeter" methods
        # In the case of "Square",
        #  the width attribute is replaced by the length attribute
        # Therefore, the "area" & "perimiter" methods of the
        #  "Square" class which are inherited from "Rectangle"
        #  will reference length for both "length" and "width"
        super().__init__(length, length)
```

Here is how you would rewrite the above code if you didn't use the `super()` method

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
```

Using `super()` to access parent methods

- You can use the `super()` method to gain access to parent methods.
- Just call `super().<parent_method>(param1, param2, ...)` to invoke a parent method in the child class

```python
# Grandparent class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Parent Class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

# Child Class
class Cube(Square):
    def surface_area(self):
        # Access / Invoke the "area()" method inherited
        #  from one of the super classes ("Rectangle")
        face_area = super().area()
        return face_area * 6

    def volume(self):
        # Access / Invoke the "area()" method inherited
        #  from one of the super classes ("Rectangle")
        face_area = super().area()
        return face_area * self.length
```

Example 2 of Inheritance in Python:

```python
# Define a User class
# This will be the parent class of the Wizard and Archer class
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print(f"logged in using email: {self.email}")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Wizard(User):
    def __init__(self, name, power, email):
        # Invoke superclass' constructor method.
        # Without this, Wizard would not have access to email from parent class
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Archer(User):
    def __init__(self, name, num_arrows, email):
        # Invoke superclass' constructor method.
        # Without this, Wizard would not have access to email from parent class
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f"Shot an arrow: arrows left - {self.num_arrows}")


# Instantiate the child classes
# Notice that although neither of the child classes had the "sign_in" method in their class definitions
#  they can still use these methods as "sign_in" is inherited from the User parent class

## Instantiate a wizard
wizard = Wizard("Merlin", 50, "magic.man@mail.com")
wizard.sign_in()  # "logged in using email: magic.man@mail.com"
wizard.attack()  # attacking with power of 50

## Instantiate an archer
archer = Archer("Robin", 100, "the.hood@mail.com")
archer.sign_in()  # "logged in using email: the.hood@mail.com"
archer.attack()  # Shot an arrow: arrows left - 99

```

#### Multiple Inheritance

While it is possible to enable multiple inheritance in Python (by passing in 2 or more parent classes into the child class), it is generally not recommended as it is too complicated to properly setup and error prone if not done correctly

### Polymorphism

`Polymorphism` is the ability of objects to take on different forms.

In Python, `polymorphism` refers to the way in which different object classes can share the same method name.

Polymorphism can be achieved by using method overriding or method overloading.

```python
# Define a User class
# This will be the parent class of the Wizard and Archer class
class User:
    def sign_in(self):
        print("logged in")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


# This class inherits from the User class
#  it is a child class / sub-class of the User class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f"Shot an arrow: arrows left - {self.num_arrows}")


## Instantiate a wizard
wizard = Wizard("Merlin", 50)

## Instantiate an archer
archer = Archer("Robin", 100)


# Declare a function which demonstrates polymorphism
# Polymorphism refers to the way in which different object classes can share the same method name
# Each class has an "attack" method (same name but different logic)
def player_attack(character):
    character.attack()


# Invoke the player_attack function by passing in the different classes
player_attack(wizard)  # attacking with power of 50
player_attack(archer)  # Shot an arrow: arrows left - 99


# Another way to demonstrate Polymorphism
# Here, we call the same method on each object in the list
for char in [wizard, archer]:
    char.attack()

# attacking with power of 50
# Shot an arrow: arrows left - 99
```

```python
# Define a parent class
class Shape:
    # Define a method with no logic
    # Logic will be implemented by the inheriting child classes
    def area(self):
        pass

# Inherit from the parent class "Shape"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Update / Overwrite the logic of inherited method
    def area(self):
        return self.width * self.height

# Inherit from the parent class "Shape"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Update / Overwrite the logic of inherited method
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(7)]
for shape in shapes:
    print(shape.area())
```

## Advanced Class Method Techniques

### Abstract Methods

To define an abstract class, it must inherit from `ABC` (`Abstract Base Class`). You will need to import `ABC` & `abstractmethod` from `abc` built-in library

```python
# Must import this to define abastract method
from abc import ABC, abstractmethod

# Inherit from Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Inherit from Shape parent class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement logic for inherited abstract method
    def area(self):
        return self.width * self.height

# Inherit from Shape parent class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement logic for inherited abstract method
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(7)]
for shape in shapes:
    print(shape.area())
```

## References

- [Real Python - OOP in Python3](https://realpython.com/python3-object-oriented-programming/)
- [Python Cheat Sheet - OOP Basics](https://www.pythoncheatsheet.org/cheatsheet/oop-basics)
- [Real Python - Supercharge your Classes with Python super()](https://realpython.com/python-super/)
- [List of Python Dunder Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
