# The constructor is the first method automatically called when you create a new object from a class. I
# ts primary purpose is to initialize (set up) the object's attributes with starting values.

# it is always named __init__ (pronounced "dunder init" for double-underscore initialization).

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = True

my_car = Car('Toyota','Camery',1989)

print(my_car.make)