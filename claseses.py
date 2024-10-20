class Restaurant :
    """A simple restaurant class"""
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name =restaurant_name
        self.cuisine_type =cuisine_type 
        self.number_served = number_served
    def describe_restaurant(self) :
        print(f"Name of the restaurant - {self.restaurant_name} and served {self.cuisine_type}")
        print(f"{self.restaurant_name} served {self.cuisine_type}")
    def open_restaurant(self) :
        print(f"{self.restaurant_name}  is now OPEN  ")
    def set_number_served(self,served) :
        self.number_served = served
    def increment_number_served(self,add_served) :
        self.number_served += add_served


class IceCreamStand (Restaurant) :
    def __init__(self,restaurant_name,cuisine_type,flavours,number_served):
        """Initialize attributes of the parentclass"""
        super().__init__(restaurant_name,cuisine_type,number_served=0)
        self.flavours = flavours 
    def display_flavours(self):
        print (f"Available flavours for {self.restaurant_name}  are : ")
        for flavour in self.flavours :
            print(f"  - {flavour}")
all_flavours = IceCreamStand('Swice', 'Creamheaven',['orange','pinapple','mango'],90)

all_flavours.display_flavours()

class User :
    def __init__(self,first_name , last_name, **other_attributes) :
        self.first_name = first_name 
        self.last_name = last_name
        self.other_attributes = other_attributes
    def describe_user(self):
        print (f"{self.first_name}, {self.last_name} ,{self.other_attributes}")
    def greet_user(self):
        print (f"Hi {self.first_name}, Good Morning")

class Admin(User) :
    """ adding attributes"""
    def __init__(self,first_name , last_name,privileges,**other_attributes) :

        super().__init__(first_name , last_name, **other_attributes)
        """initializing attributes"""
        self.privileges = privileges
    def show_privileges(self) :
        print(f"List of Administrator privileges : ")
        for privilege in self.privileges :
            print(f"- {privilege}")
admin_user= Admin('john','doe',["can add post", "can delete post", "can ban user",'can creat user'])
admin_user.show_privileges()


class User:
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
        for privilege in self.privileges:
            print(f"- {privilege}")
        
        
class Admin(User):
    """Admin class inherits from Users."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        super().__init__(first_name, last_name, **other_attributes)
        self.privileges = Privileges()  # Create an instance of Privileges class

# Creating an Admin instance and assigning privileges
admin_user_1 = Admin('John', 'Doe')
admin_user_1.privileges.privileges = ["can add post", "can delete post", "can ban user",'can creat user']
admin_user_1.privileges.show_privileges()
