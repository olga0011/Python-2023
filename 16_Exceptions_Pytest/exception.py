'''1. Function that takes two integer inputs from the user and calculates their division'''

class InvalidInputError(Exception):
    pass

def divide_numbers():
    try:
        num1 = int(input("Please enter a first number: "))
        num2 = int(input("Please enter a second number: "))

        if num2 == 0:
            raise ZeroDivisionError
        
        result = num1 / num2

    except ValueError:
        raise InvalidInputError("Error: Invalid input. Please enter whole numbers only, without quotation marks")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please try again")
        return divide_numbers() #after a zero-division error the program will start once again

    return result

try:
    print(divide_numbers())
except InvalidInputError as e: #custom exception
    print(e)
