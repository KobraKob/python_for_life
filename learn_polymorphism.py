# Polymorphism in Python means "same operation, different behavior." 
# It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.

# The Analogy
# Think of the Play Button on a remote.
# If you point it at a TV, it starts a movie.
# If you point it at a Music Player, it plays a song.
# The Button (Interface): Same ("Play").
# The Result (Action): Different.
#To do this -- METHOD OVERRIDING also called RUNTIME polymorphism

class Birds:
    def fly(slef):
        return 'Some birds can fly'

class Sparrow(Birds):
    def fly(self):
        return 'I Fly High'

class Chicken(Birds):
    def fly(self):
        return 'I cannot fly'

bird1 = Sparrow()
bird2 = Chicken()

print(bird1.fly())
print(bird2.fly())


#DUCK TYPPING
# What: Python doesn't care about the object's type (class name); it only cares if the object has the specific method (function) you are trying to call.
# Principle: "If it walks like a duck and quacks like a duck, then it is a duck."

class Dog:
    def speak(self): return 'Woof'

class Human:
    def speak(self): return 'Hello!'

def in_forest(someone):
    print(someone.speak())

in_forest(Dog())
in_forest(Human())  
