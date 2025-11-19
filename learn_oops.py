#Python OOP Concepts
# OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. 
# In OOP, object has attributes thing that has specific data and can perform certain actions using methods.

# Class
# A class is a collection of objects. Classes are blueprints for creating objects. 
# A class defines a set of attributes and methods that the created objects (instances) can have.

#Creating Class
class Dog:
    species = 'Canine'

    def __init__(self,name,age):
        self.name = name
        self.age = age

# class Dog: Defines a class named Dog.
# species: A class attribute shared by all instances of the class.
# __init__ method: Initializes the name and age attributes when a new object is created.


# Objects
# An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

# An object consists of:

# State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

#Creating object for dog class
dog1 = Dog('Tiger',11)
print(dog1.name)
print(dog1.age)
print(dog1.species)


print('------------------------------------------------------------------------------------------------------------------------------------------------------------')

class Feline:
    animal = 'Tiger'

    def __init__(self,name,age):
        self.name = name
        self.age = age

tiger1 = Feline('Chibbi',18)
tiger2 = Feline('Chan-Chan',14)
print(tiger1.name)
print(tiger1.age)
print()
print(tiger2.name)
print(tiger2.age)
print()
print('------------------------------------------------------------------------------------------------------------------------------------------------------------')


# Inheritance
# Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.


class Device:
    def power(self):
        return 'The Device is on'
    

class Phone(Device):
    def call(self):
        return 'Making a call'

class Camera(Device):
    def take_photo(self):
        return 'Taking Photo'

class Landline(Phone):
    def connect_wire(self):
        return 'Connected to landline'

class Smartphone(Phone,Camera):
    def use_app(self):
        return 'Opening App'

iphone = Smartphone()
sony = Camera()
samsung = Phone()

print(iphone.power())
print(iphone.use_app())

print(sony.take_photo())

print(samsung.call())

print('------------------------------------------------------------------------------------------------------------------------------------------------------------')

