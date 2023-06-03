class Vehicle:
    '''Parent class with a constructor and repr function to create and print an object'''

    max_speed = 0
    mileage = 0

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(str(self.max_speed), " ", str(self.mileage))

    def seating_capacity(self, capacity):
        result = (
            "The seating capacity of "
            + self.__class__.__name__
            + " is "
            + str(capacity)
            + "."
        )
        print(result)


v1 = Vehicle(120, 4000)
v1.print_vehicle()
v1.seating_capacity(5)


class Bus(Vehicle):
    '''Child class Bus inherits all of the variables and methods of the Vehicle class'''

    counter = 0

    def __init__(self, max_speed, mileage):
        '''Use a constructor of a parent class and add a child-property "color" with a default value'''
        '''Set the color of all Buses to red when at least 5 of them are created'''
        super().__init__(max_speed, mileage)
        Bus.counter += 1
        if Bus.counter <= 5:
            self.color = "white"
        else:
            self.color = "red"

    def seating_capacity(self, capacity=50):
        '''Use a parent method, but add a default value 50. If called with an argument, the value will change'''
        super().seating_capacity(capacity)


b1 = Bus(100, 6000)
b1.print_vehicle()
print(b1.color)
b1.seating_capacity()
b1.seating_capacity(20)

'''Bonus'''
b2 = Bus(100, 6000)
b3 = Bus(100, 6000)
b4 = Bus(100, 6000)
print(b4.color)  # white
b5 = Bus(100, 6000)
print(b5.color)  # white
b6 = Bus(100, 6000)
print(b6.color)  # red
