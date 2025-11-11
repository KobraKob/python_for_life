mylist = ["apple",'orange','pineapple']
print(mylist)

#length function
anime = ['black clover','naruto','demon slayer','one piece']
print(len(anime))

#Access Items
print(anime[2])
print(anime[-1])

#Range of Indexes
cars = ["BMW", "Audi", "Benz", "Tata"]
print(cars[0:3])

#Check if Item Exists
thislist = ['naanu', 'neenu', 'avanu', 'avalu']
if 'avanu' in thislist:
    print('yes avanu is in the list')

#Change Item Value
somelist = ['apple', 'google', 'microsoft', 'accenture']
somelist[2] = 'amazon'
print(somelist)

#Insert Items
otherlist = ["mouse", 'keyboard', 'display', 'speaker']
otherlist.insert(1,'gamepad')
print(otherlist)

#Append (end of list)
clocr = ['red', 'orange']
clocr.append('blue')
print(clocr)

something = ['eye', 'ear', 'mouth']
otherthing = ['hand', 'legs', 'fingers']
something.extend(otherthing)
print(something)

#Remove 
country = ['India', 'USA', 'Australia', 'canada', 'pakisthan']
country.remove('pakisthan')
print(country)

#Remove Specified Index
tree = ['branch', 'leaves', 'root', 'steam']
tree.pop(1)
print(tree)

tree.clear()
print(tree)



#Loop Through a List
city = ['bengaluru', 'mysuru', 'hubli', 'belagavi']
for c in city:
    print(c)

dogs = ['german sheaperd', 'shitzu', 'pomoriean', 'husky']
i = 0
while i < (len(dogs)):
    print(dogs[i])
    i = i+1

#List Comprehension
vehicles = ['car', 'bike', 'auto', 'plane']
newVehicle = [x for x in vehicles if 'a' in x]
print(newVehicle)

#Sort List 
mobiles = ['apple', 'samsung', 'moto', 'vivo'] 
mobiles.sort()
print(mobiles)
mobiles.sort(reverse=True)
print(mobiles)


#Join lists
laptop = ['asus tuf', 'macbook', 'vivobook', 'msi']
pc = ['samsunng', 'macintosh', 'acer']
computer = laptop + pc
print(computer)






#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list