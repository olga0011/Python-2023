'''1: Closure - Calculator'''

'''Closure function, that performs basic arithmetic operations'''
def calculator():
    def operate(num1, operation, num2):
        try:    
            if (operation == "add"):
                return num1 + num2
            elif (operation == "sub"):
                return num1 - num2
            elif (operation == "mult"):
                return num1 * num2
            elif (operation == "div"):
                try:
                    return num1 / num2
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")
            else:
                print("That was not a valid operation. Please use 'add', 'sub', 'mult' or 'div' instead.")
                return None
        except TypeError:
            print("TypeError: At least one argument is not a valid number.")
    return operate #calculator fuction reterns operate function 

calc = calculator() #Create a calculator instance by calling the calculator() function

'''Call the returned function from the calculator instance, providing different numbers and
operations, and print the results. '''
print(str(calc(-1, "add", 2))) # 1
print(str(calc(-1, "sub", 2))) # -3
print(str(calc(-1, "mult", 2))) # -2
print(str(calc(-1, "div", 2))) # -0.5
print(str(calc(-1, "test", 2))) # That is not a valid operation. Please use 'add', 'sub', 'mult' or 'div' instead. None 
print(str(calc(1, "div", 0))) # Error: Cannot divide by zero. None
print(str(calc(1.75, "add", 3.25))) # 5.0
print(str(calc(5, "mult", "3"))) # 33333
print(str(calc("str", "div", 67))) # At least one argument is not a valid number. None
print(str(calc(7, "sub", "4"))) # At least one argument is not a valid number. None


'''3: Special Methods - Rectangle'''

class Rectangle:
    '''Class Rectangle with attributes width and height'''
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self): # special method to return a string representation of the rectangle
        return f"Rectangle: {self.width} {self.height}"
    
    def __eq__(self, other): # special method to compare two rectangles for equality
        if isinstance(other, Rectangle):
            return ((self.width==other.width)and(self.height==other.height))
        return False

'''test the string representation of multiple Rectangle objects'''    
r1 = Rectangle(3, 2)    
print(r1)
r2 = Rectangle(2, 3)
print(r2)
r3 = Rectangle(3, 2)
print(r3)

class Triangle: 
    '''Class Rectangle with attributes width and height to test the __eq__() special method later'''
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self): # special method to return a string representation of the triangle
        return f"Triangle: {self.width} {self.height}"    

'''test the string representation of Triangle object with the same width and height'''    
t1 = Triangle(3, 2)
print(t1)

'''test equality comparison: returns False in case of different classes (Rectangle and Triangle) even if the width and height are the same'''
print(r1 == r2) # False
print(r1 == r3) # True
print(t1 == r1) # False
