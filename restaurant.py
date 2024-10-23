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
