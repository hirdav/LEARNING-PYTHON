# Exercise 9-6: Ice Cream Stand
class Restaurant:
    """A simple restaurant class."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}, Cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now OPEN.")
    
    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, add_served):
        self.number_served += add_served

class IceCreamStand(Restaurant):
    """An ice cream stand that inherits from the Restaurant class."""
    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialize attributes of the parent class and flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def display_flavours(self):
        """Display the list of available ice cream flavors."""
        print(f"Available flavors for {self.restaurant_name}:")
        for flavour in self.flavours:
            print(f"  - {flavour}")

# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand('Swice', 'Creamheaven', ['orange', 'pineapple', 'mango'])
ice_cream_stand.display_flavours()


# Exercise 9-7 & 9-8: Admin Class with Privileges Class
class Users:
    """A simple user class."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.other_attributes = other_attributes

    def describe_user(self):
        """Describe the user."""
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.other_attributes.items():
            print(f"{key}: {value}")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name}!")

class Privileges:
    """A class to manage privileges of an admin."""
    def __init__(self, privileges=[]):
        """Initialize privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- No privileges assigned")

class Admin(Users):
    """Admin class inherits from Users and includes privileges."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        super().__init__(first_name, last_name, **other_attributes)
        self.privileges = Privileges()  # Create an instance of Privileges class

# Creating an Admin instance and assigning privileges
admin_user = Admin('John', 'Doe')
admin_user.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin_user.privileges.show_privileges()
