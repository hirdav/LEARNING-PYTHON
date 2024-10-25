class Privileges:
    """A class to manage privileges of an admin."""
    def __init__(self, privileges=[]):
        """Initialize privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        
        for privilege in self.privileges:
                print(f"- {privilege}")
                