"""Task 1 Scope and Namespace"""

def calculate_price(quantity, price):
    '''Defines a function, which calculates price based on initial price, quantity and discount'''
    total_price = quantity * price
    discount = 0.1

    def apply_discount(price):
        '''Define a nested function called apply_discount() within the calculate_price() function 
        and return the discounted price'''
        price = price * discount
        return price

    #Discount will be appled of the total price. Return the discounted price
    price = apply_discount(total_price)
    return price


print(calculate_price(5, 10))

# Local variables are declared inside the function, limited to their function 
# and are lost when the function ends.
# Global variables are declared outside of every function of the program, 
# that's why they are accessible by all functions in a program. 
# They are created as execution of the program begins and are lost when the program is ended.