"""
Assingment OOPS
What Is Object-Oriented Programming?
Object-Oriented Programming(OOP), is all about creating “objects”. 
An object is a group of interrelated variables and functions. 
These variables are often referred to as properties of the object and functions are referred to as the behavior of the objects. 
These objects provide a better and clear structure for the program.

For example, a car can be an object. If we consider the car as an object then its properties would be –
 its color, its model, its price, its brand, etc. And its behavior/function would be acceleration, slowing down, gear change.

Class: Class is blue print of object

A class is a code template for creating objects. Objects have member variables and have behaviour associated with them.
 In python a class is created by the keyword class.

An object is created using the constructor of the class.
 This object will then be called the instance of the class. 
 In Python we create instances in the following manner
For example, let's create a simple, empty class with no functionalities.

 class student:
     pass
 
 student = student()
 print(student)

 2. Objects 
When we define a class only the description or a blueprint of the object is created.  
There is no memory allocation until we create its object. 
The objector instance contains real data or information.

Instantiation is nothing but creating a new object/instance of a class. Let’s create the object of the above class we defined-

class Person:
   def __init__(self, name, age):
   self.name = name
   self.age = age

   def myfunc(self):
   print("Hello my name is " + self.name)

x = Person("Aryan", 16)
x.myfunc()


The 4 principles of OOPS [each with example]
I- Method
The method is a function that is associated with an object. 
In Python, a method is not unique to class instances. Any object type can have methods.
class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

II-Inheritance
Inheritance is the most important aspect of object-oriented programming, which simulates the real-world concept of inheritance. 
It specifies that the child object acquires all the properties and behaviors of the parent object.
By using inheritance, we can create a class which uses all the properties and behavior of another class. 
The new class is known as a derived class or child class, and the one whose properties are acquired is known as a base class or parent class.

class Person:
   def __init__(self, fname, lname):
   self.firstname = Veer
   self.lastname = kumar

   def printname(self):
   print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

j1 = Person("Veer", "Aryan")
j1.printname()


III-Polymorphism
Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape.
 By polymorphism, we understand that one task can be performed in different ways.
Polymorphism can be static and dynamic. Static is achieved by method overloading, 
and dynamic by method overriding.
 For example -

  
def add(x, y, z = 0): 
   return x + y+z
  
 
print(add(2, 3))
print(add(2, 3, 4))


Encapsulation:
Encapsulation is also an essential aspect of object-oriented programming. 
It is used to restrict access to methods and variables. In encapsulation,
code and data are wrapped together within a single unit from being modified by accident

Example.
class employee(object):
def __init__(self):   
self.name = Ram
self._age = 27
self.__salary = 12,000
 
object1 = employee()
print(object1.name)
print(object1._age)
print(object1.__salary)


IV-Data Abstraction:
Data abstraction and encapsulation both are often used as synonyms. 
Both are nearly synonyms because data abstraction is achieved through encapsulation.

Abstraction is used to hide internal details and show only functionalities. 
Abstracting something means to give names to things so that the name captures
 the core of what a function or a whole program does.

Example:

from abc import ABC, abstractmethod

class employee(Aryan):
def emp_id(self,id,name,age,salary):    //Abstraction
pass
 
class childemployee1(employee):
def emp_id(self,id):
print("emp_id is 123")
 
emp1 = childemployee1()
emp1.emp_id(id)




4.Inheritance in Python Class
Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as Parent class. And the class that inherits the properties from the parent class is the Child class.

The interesting thing is, along with the inherited properties and methods, a child class can have its own properties and methods.

How to inherit a parent class? Use the following syntax:

class parent_class:
body of parent class

class child_class( parent_class):
body of child class


Single Inheritance:
Single inheritance enables a derived class to inherit properties from a single parent class, 
thus enabling code reusability and the addition of new features to existing code.

# Base class
class Parent:
     
    def func1(self):
       print("This function is in parent class.")
 
# Derived class
class Child(Parent):
    def func2(self):
       print("This function is in child class.")
 

object = Child()
object.func1()
object.func2()

Multiple Inheritance: 
When a class can be derived from more than one base class this type of inheritance
 is called multiple inheritance. 
In multiple inheritance,all the features of the base classes are inherited
 into the derived class.
 
 # Example of multiple inheritance
 

# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
      print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
      print("Father :", self.fathername)
      print("Mother :", self.mothername)
 

love = Son()
love.fathername = "Rajendra"
love.mothername = "Soni"
love.parents()


"""