#Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a=33
b=200
if a<b:
    print("yep it is less")

number = 10
if number > 0:
    print("the number is postive")

is_logged = True
if isinstance:
    print("Welcome")

#The Elif 
a = 30
b = 30
if a > b:
    print("a is greater")
elif a < b:
    print("a is less than b")
else:
    print("Equal")

x=20
y=30
max = x if x>y else y
print(max)

username = "naanu"
display_name = username if username else "Guest"
print("Welcome,", display_name)
