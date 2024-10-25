class Admin(User):
    """Admin class inherits from Users."""
    def __init__(self, first_name, last_name, **other_attributes):
        """Initialize the Admin class with user attributes and privileges."""
        super().__init__(first_name, last_name, **other_attributes)
        self.privileges = Privileges()