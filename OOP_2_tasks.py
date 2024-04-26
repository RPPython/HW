# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Create a base class called 'Animal' to represent a general animal. The class should have the following attributes and methods:

    Attributes:
    - 'species': a string representing the species of the animal.
    - 'age': an integer representing the age of the animal.

    Methods:
    - 'sound()': a method that returns the string 'Sound not defined.'

    Create two subclasses, 'Dog' and 'Cat', that inherit from the 'Animal' class.
    Each subclass should override the 'sound()' method to return 'Bark' for Dog and 'Meow' for Cat.
"""

### YOUR CODE HERE:
# class Animal():
#     def __init__(self, species: str, age: int) -> None:
#         self.species = species
#         self.age = age

#     def sound(self):
#         return 'Sound not defined'
    
# class Dog(Animal):
#     def sound(self):
#         return "Bark"

#     # def __init__(self, species: str, age: int) -> None:
#     #     super().__init__(species, age)
#     #     print( f'My animal {self.species}, he is {self.age} and his sound is {"Bark"} ')

# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    

# my_dog = Dog("Canine", 5)
# my_cat = Cat('Feline', 3)

# print(my_dog.sound())
# print(my_cat.sound())


### TEST:
# my_dog = Dog("Canine", 5)
# my_cat = Cat("Feline", 3)
# print(my_dog.sound())
# print(my_cat.sound())

### EXPECTED OUTPUT:
# "Bark"
# "Meow"


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Extend the 'Animal' class from Task 1 by adding a subclass 'Bird' that includes
    an additional attribute 'can_fly' (a boolean). Override the 'sound()' method to
    return 'Chirp Chirp' if the bird can fly.
"""

### YOUR CODE HERE:

# class Animal():
#     def __init__(self, species, age) -> None:
#         self.species = species
#         self.age = age

#     def sound(self):
#         return 'Sound not defined'

# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# class Bird(Animal):
#     def __init__(self, species, age, can_fly) -> None:
#         super().__init__(species, age)
#         self.can_fly = can_fly

#     def sound(self):
#         if self.can_fly:
#             return "Chirp Chirp"
#         else:
#             return "Sound not defined"
        
# parrot = Bird("Parrot", 2, can_fly=True)
# penguin = Bird("Penguin", 5, can_fly= False)

# print(parrot.sound())
# print(penguin.sound())


### TEST:
# parrot = Bird("Parrot", 2, can_fly=True)
# penguin = Bird("Penguin", 5, can_fly= False)

# print(parrot.sound())
# print(penguin.sound())

### EXPECTED OUTPUT:
# Chirp Chirp
# Sound not defined.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a base class 'Vehicle' with attributes 'make' and 'model'. 
Add a method 'info()' that returns a string containing the make and model.

Create a subclass 'Bicycle' that inherits from 'Vehicle' 
and adds an attribute 'gear_count'. 
Override the 'info()' method to include the number of gears.
"""

### YOUR CODE HERE:

# class Vehicle():
#     def __init__(self, make, model) -> None:
#         self.make = make
#         self.model = model

#     def info(self):
#         return "{}, ' ', {}".format(self.make, self.model) 
    
# class Bicycle(Vehicle):
#     def __init__(self, make, model, gear_count) -> None:
#         super().__init__(make, model)
#         self.gear_count = gear_count
        
#     def info(self):
#         if self.gear_count:
#             return "{} {} with {} gears".format(self.make, self.model, self.gear_count) 
    
# my_bike = Bicycle("Trek", "Marlin 5", 21)
# print(my_bike.info())   

### TEST:
# my_bike = Bicycle("Trek", "Marlin 5", 21)
# print(my_bike.info())

### EXPECTED OUTPUT:
# "Trek Marlin 5 with 21 gears"


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a base class called 'Shape' to represent a geometric shape. 
The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the name of the shape.

Methods:
- 'area()': a method that will return the string 'Not implemented for common shape'

Create two subclasses, 'Rectangle' and 'Circle', 
that inherit from the 'Shape' class and implement their specific area calculation methods.
"""

### YOUR CODE HERE:

# import math

# class Shape():
#     def __init__(self, name:str) -> None:
#         self.name = name
    
#     def area(self):
#         return "Not implemendted for common shape"
    
# class Rectangle(Shape):
#     def __init__(self, name: str, width, height) -> None:
#         super().__init__(name)
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, name: str, radius) -> None:
#         super().__init__(name)
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2
        

        


# # TEST:
# rectangle1 = Rectangle("Rectangle", 5.0, 3.0)
# circle1 = Circle("Circle", 2.0)

# print(rectangle1.area())
# print(f'{circle1.area():.2f}')

# EXPECTED OUTPUT:
# 15.0
# 12.56637

# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Implement a class 'Building' that stores the number of floors and the year built. 
Include a method 'description()' that summarizes the building's details.

Create a subclass 'Office' that inherits from 'Building' 
and adds an attribute for the number of offices. 
Override 'description()' to include this new information.
"""

### YOUR CODE HERE:

# class Building():
#     def __init__(self, floors_number, year_built) -> None:
#         self.floors_number = floors_number
#         self.year_built = year_built
        
#     def description(self):
#         return "Building with {} floors, built in {}.".format(self.floors_number, self.year_built)
    
# class Office(Building):
#     def __init__(self, floors_number, year_built, offices_number) -> None:
#         super().__init__(floors_number, year_built)
#         self.offices_number = offices_number

#     def description(self):
#         return f'Office building with {self.floors_number} floors and {self.offices_number} offices, built in {self.year_built}'
#         ## base_discription = super().description()
#         ## return f'Offise {base_discription} and {self.offices_number} offies'

# ### TEST:
# my_house = Building(2, 1930)
# my_office = Office(10, 1998, 200)

# print(f'My house is {my_house.description()}')
# print(f'My office is {my_office.description()}')

### EXPECTED OUTPUT:
# "My house is Building with 2 floors, built in 1930."
# "My office is Office building with 10 floors and 200 offices, built in 1998."
