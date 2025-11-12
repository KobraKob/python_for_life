#dictionary is a collection which is ordered*, changeable and do not allow duplicates.

this_dict = {
    'name': "naanu",
    'age': '22',
    'virgin': True
}
print(this_dict['virgin'])
name = this_dict['name']
print(name)
x = this_dict.items()
print(x)

this_dict['girl'] = 'Nope'
print(this_dict)    
print()

for a in this_dict:
    print(this_dict[a])
print()

for r,t in this_dict.items():
    print(r,t)


students = {
    'boys':{
        'name':'harper',
        'age':32,
        'place':'texas'
    },
    'girls':{
        'name':'nancy',
        'age':22,
        'place':'new york'
    }
}

for q, obj in students.items():
    print(q)

    for z in obj:
        print(z + ':',obj[z])