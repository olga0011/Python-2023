'''Task 1'''
class Car:
    '''Class with a constructor and repr function to create and print an object'''
    brand = ""
    model_name = ""
    construction_year = 0

    '''Task 3'''
    def __init__(self, brand, model_name, construction_year):
        self.brand = brand
        self.model_name = model_name
        self.construction_year = construction_year

    def __repr__(self):
        return ("Car brand: "+ self.brand + " model name " + str(self.construction_year))
    
'''Task 2 - have to comment this part to be able to run the file'''
#car1 = Car()
#car1.brand = "porsche"
#car1.model_name = "cayenne"
#car1.construction_year = 2019
#print(car1.brand, car1.model_name, str(car1.construction_year))

'''Task 3'''
car2 = Car("porsche2", "cayenne2", 2020)
print(car2)
