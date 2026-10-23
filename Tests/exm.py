#!/usr/bin/python3 
"""
class Car :
    def __init__(self, color , brand , model):
        self.color = color 
        self.brand = brand 
        self.model = model 

    def get_info(self):
        return f' this is {self.brand}{self.model} with the color {self.color} , clear the way!'
    def __str__(self):
        return 


class AnObj :
    def __init__(self, h , l):
        self.h = h 
        self.l = l 

    def Space(self):
        return self.h * self.l 

        """

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self):
        return f'{self.x} + {self.y}'
    
    def __str__(self):
        return f'{self.x} and {self.y} '

    def __repr__(self):
        # Aim for unambiguous, developer-friendly output
        # Often looks like the code to create the object
        return f"Point(x={self.x}, y={self.y})"

# Create an instance
p2 = Point(5, -3)

# Since __str__ is missing, rpint() and str() fall back to __repr__

print(p2)         # Calls __str__ (falls back to __repr__)
add(p2)
#print(str(p2))     # Calls __str__ (falls back to __repr__)
#print(repr(p2))    # Calls __repr__
