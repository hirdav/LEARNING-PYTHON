# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

# admin_privileges.py

  # Import User class from user.py


class Admin(User):
    """Admin class inherits from User."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        super().__init__(first_name, last_name, **other_attributes)
        self.privileges = Privileges()  # Create an instance of Privileges class
