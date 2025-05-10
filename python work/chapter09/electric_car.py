#class ElectricCar(Car):
    #"""Represent aspects of a car, specific to electric vehicles."""
 
def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())  

 # self.battery_size = 40
def describe_battery(self):
    """Print a statement describing the battery size."""
#print(f"This car has a {self.battery_size}-kWh battery.")
#my_leaf.describe_battery()

#class ElectricCar(Car):
 #def fill_gas_tank(self):
  #      """Electric cars don't have gas tanks."""
   #     print("This car doesn't have a gas tank!")