#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ('apple','orange','banana')
print((thistuple))
print(type(thistuple))

cars = ('maruthi','honda','hundai','tata')
for car in cars:
    print(car)
print()


students = ('Raj','Roy','Anna','Bob')
i=0
while i<(len(students)):
    print(students[i])
    i = i+1
print()
country = ('India','USA','canada')
print(country)
print()

#Change Tuple Values
#convert the tuple into a list, change the list, and convert the list back into a tuple.
numbers = ('one','two','three','four')
numbers_t = list(numbers)
numbers_t[0] = 'zero'
new_numbers = tuple(numbers_t)
print(new_numbers)
    