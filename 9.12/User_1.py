# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

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