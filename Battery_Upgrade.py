"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 65 if it isn’t already. Make 
an electric car with a default battery size, call get_range() once, and then 
call get_range() a second time after upgrading the battery. You should see an 
increase in the car’s range."""


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
class Battery :
    def __init__ (self,battery_size=40):
        """intialize attributes for battery"""  
        self.battery_size = battery_size
        
    def describe_battery (self) :
        """printing a statement of describing battery size"""
        print(f"this car has a {self.battery_size}kwh battery ")
    def get_range(self):
        """statement about the range this battery provide"""
        if self.battery_size==40 :
            range=150
        elif self.battery_size ==65 :
            range = 225 
        print (f"This car can go {range}")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
 

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        """Instances as attribute* also we have for various info regarding battery """
        """so battery moved with a class above for effciency """
        """however electic car need the battery attribute so its dialed up here."""
        """and also called composition"""
        self.battery=Battery() 

    def describe_battery (self) :
        """printing a statement of describing battery size"""
        print(f"this car has a {self.battery_size}-- kwh battery ")
    def fill_gas_tank(self):
        print("This cars doesn't need a gas tank")
my_leaf = ElectricCar ('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()