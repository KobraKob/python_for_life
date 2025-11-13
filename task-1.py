#Task:
#Write a Python script that reads 10 employee records from a list of dicts & prints employees with salary > X.

employees = [
    {'name':'luffu','depatment':'pirate','salary':50000},
    {'name':'asta','depatment':'magic','salary':35000},
    {'name':'naruto','depatment':'ninja','salary':40000},
    {'name':'anos','depatment':'demon','salary':5000000},
    {'name':'denji','depatment':'perv','salary':10000},
    {'name':'tanjiro','depatment':'slayer','salary':23903},
    {'name':'shikamaru','depatment':'ninja','salary':34902},
    {'name':'minato','depatment':'hukage','salary':60000},
    {'name':'rimaru','depatment':'king','salary':1000000},
    {'name':'naanu','depatment':'developer','salary':13000},
]

x =int(input("what should be the threashold for the salary "))
for emp in employees:
    if emp['salary'] > x:
        print(emp)
