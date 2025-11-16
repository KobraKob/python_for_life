# Import module in Python

# In Python, modules help organize code into reusable files. 
# They allow you to import and use functions, classes and variables from other scripts. T
# he import statement is the most common way to bring external functionality into your Python program.

import math
import pandas as pd
pi = math.pi
print(pi)

#external Modules
data = {
    "Name": ['Gabbar',"Singham",'Tuntun'],
    "Age": [28,32,39]
}

rep = pd.DataFrame(data)
print(rep)


things = ["Laptio", 'chairs', 'fridge','mobile']
thing = pd.DataFrame(things)
print(thing)