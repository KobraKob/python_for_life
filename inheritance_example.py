# Create a base class Vehicle with a method start_engine() that returns "Engine started".

# Create a subclass Car that inherits from Vehicle and adds a method play_radio() returning "Playing radio".

# Create another subclass Bike that inherits from Vehicle and adds a method kick_start() returning "Kick start engaged".

# Create one object of Car and one object of Bike.

# Print the result of:

# start_engine() for both

# play_radio() for the car

# kick_start() for the bike


class Vehicle:
    def start_engine(self):
        return 'Engine Started'

class Car(Vehicle):
    def play_radio(self):
        return 'Playing Radio'

class Bike(Vehicle):
    def kick_start(self):
        return 'Kick Start engaged'

audi = Car()
apache = Bike()

print(audi.start_engine())
print(audi.play_radio())
print(apache.start_engine())
print(apache.kick_start())