
# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from User_1 import User
class Privileges:
    """A class to manage privileges of an admin."""
    def __init__(self, privileges=[]):
        """Initialize privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        
        for privilege in self.privileges:
                print(f"- {privilege}")
class Admin(User):
    """Admin class inherits from Users."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        self.first_name=first_name
        self.last_name=last_name
        self.other_attributes=other_attributes
        self.privileges = Privileges()