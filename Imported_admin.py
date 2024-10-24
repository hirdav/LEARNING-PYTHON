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
        print("Privileges: ")
        for privilege in self.privileges:
                print(f"- {privilege}")
        

class Admin(Users):
    """Admin class inherits from Users."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        super().__init__(first_name, last_name, **other_attributes)
        self.privileges = Privileges()  # Create an instance of Privileges class

# Creating an Admin instance and assigning privileges
admin_user = Admin('John', 'Doe')
admin_user.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin_user.privileges.show_privileges()

