# Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. 
# Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

n = 10
try:
    result = n/0
except ZeroDivisionError:
    print("Cant divide by zero")
    
# Syntax and Usage

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.


try:
    
    x = int('lowda') 
    print("Conversion successful:", x)
    
except ValueError:
    print("Oops! You cannot convert that text into a number.")

else:
    print('What are you trying to do you dumb fuck')
finally:
    print("Program finished successfully.")


# Raise an Exception
# We raise an exception in Python using the raise keyword followed by an instance of the exception class that we want to trigger.
# We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.

def set(age):
    if age < 0:
        raise ValueError('Age can not be less than 0 you dummy..!')
    print(f'the age is  {age}')

try:
    set(-2)
except ValueError as e:
    print(e)


#Custom Exception
# A Custom Exception is when you create your own specific error type instead of using Python's built-in ones

# To create a custom exception, you define a new Class that inherits from Python's standard Exception

class NegativeMoneyError(Exception):
    pass

def withdraMoney(amount):
    if amount < 0:
        raise NegativeMoneyError("Your balance can not have a negative number")

try:
    withdraMoney(-1000)
except NegativeMoneyError as e:
    print(f"Security Alert {e}")

else:
    print("Successfully Withdrawn")

finally:
    print('HAve a nice day')
 