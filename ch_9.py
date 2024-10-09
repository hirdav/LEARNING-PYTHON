class Dog:
    """A Simple attempt to model a dog"""

def __init__(self,name,age) :
        """"Initialze name and age attributes"""
        self.name = name 
        self.age = age
def sit (self) :
    """Simulate a dog sitting in response to a command."""
    print (f"{self.name} is now sitting.")

def roll_over(self):
    """Simulate rolling over in response to a command"""
    print (f"{self.name} rolled over !")


    my_dog = Dog('will',9)
    my_dog= Dog('oh',8)
    print(f"My dog name is {my_dog.name}")
    print(f"My dog  is {my_dog.age} years old.")

    my_dog.sit()
    my_dog.roll_over()
    my_dog.name()

    your_dog= Dog('olli',3)

    your_dog.roll_over()
    your_dog.name()