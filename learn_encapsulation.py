# . What is Encapsulation?
# It is the process of bundling data (attributes) and the methods (functions) that operate on that data into a single unit (the class). 
# More importantly, it involves data hiding, restricting direct access to the data from outside the class to prevent accidental modification.


# _variable	Single Underscore - Protected (By convention only). It means, "Don't touch this from outside the class," but Python won't stop you.
# __variable	Double Underscore - Pseudo-Private (Uses Name Mangling). Python internally changes the name to make it harder to access, but it's not truly hidden.
class BankAccout:
    def __init__(self,initial_balance):
        self.__balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print('Deposited successfullt')
        else:
            return 'Invalid amount'

    def get_balance(self):
        return self.__balance

account = BankAccout(200)
account.deposit(122)
print(account.get_balance())



#With Getters and Setters

class Studen:
    def __init__(self,marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,new_marks):
        if 0 <= new_marks <=100:
            self.__marks = new_marks
        else:
            return 'Error: You fuck grade must be between 0 and 1oo'

naanu = Studen(100)

print(naanu.marks)
