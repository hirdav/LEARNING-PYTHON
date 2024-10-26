class Users1:
    """A simple user class."""
    def __init__(self,first_name,last_name,age,location):
        """Initialize user attributes."""
        self.first_name= first_name 
        self.last_name= last_name
        self.age=age
        self.location = location

    def describe_user(self):
        """Describe the user."""
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.other_attributes.items():
            print(f"{key}: {value}")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name}!")

class Privileges :
    def __init__(self,privileges) :
        self.privileges = privileges
    def show_privileges(self) :
        for privileges in self.privileges :
            print(f"{privileges}")

class Admin(Users1):
    def __init__(self,first_name,last_name,age,location,privileges) :
        self.first_name= first_name 
        self.last_name= last_name
        self.age=age
        self.location = location
        self.privileges=Privileges(privileges)
newio= Admin('r','y','w','r',['e','g','q'])
newio.privileges.show_privileges()