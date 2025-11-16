#A function is a block of code which only runs when it is called.
#Creating a Function
#In Python, a function is defined using the def keyword, followed by a function name and parentheses

def gree():
    print('Hello World..!')

gree()

def name():
    return 'hello  there'
msg = name()
print(msg)

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_fun(name):
    print(name)
print(my_fun)

my_fun('Cassy')

def colect_names(f_name,l_name):
    print(f_name,"",l_name)
colect_names('balavanth','krishnana')

animals = ['dog','cat','lion','gecoko','crocodile']

def loop_animals(animals):
    for animal in animals:
        print(animal)

loop_animals(animals)

#Return Values

def add(x,y):
    return x+y
result = add(6,6)
print(result)


# Python *args
def kids_name(*name):
    print("the younger is ",*name)
kids_name("naanu")


# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:

def get_first_last(**kid):
    print('his last name is', kid['last_name'])
get_first_last(first_name = 'naanu', last_name = 'naane')



def get_details(user_name, **details):
    print('Username is' ,user_name)
    print('Additional details are')
    for key, value in details.items():
        print('', key + ',', value)

get_details('Rocky', age =25, city = 'Bengaluru', email ='rocky@somemail.com')


#Lambda
#A lambda function is a small, anonymous function defined without a name. It is used when a short, 
# one-off function is needed and defining a full def function would be unnecessary.
square = lambda x: x*x
print(square(45)
      )

#Recurrsion
#Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems of the same type.

# Core idea:
# A base case stops the recursion.
# A recursive case reduces the problem and calls the function again.

def countdown(n):
    if n <=0:
        print("Done")
    else:
        print(n)
        countdown(n-1)
countdown(10)

#Fibonacci Sequence
def fibinochi(n):
    if n <= 1:
       return n
    else:
        return fibinochi(n-1) + fibinochi(n-2)
print(fibinochi(36))

#Generators
# A generator is a type of function that produces a sequence of values lazily, yielding one value at a time instead of creating the entire sequence in memory.

def count_upto(n):
    i = 1
    while i<=n:
        yield i
        i+=1
gen =count_upto(10)
for some in gen:
    print(some)