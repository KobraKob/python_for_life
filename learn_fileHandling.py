# Reading JSON from a file using Python
# Using json.load() 
# The JSON package has json.load() function that loads the JSON content from a JSON file into a dictionary

import json
with open("sample.json","r") as f:
    data = json.load(f)
print(data)
print(type(data))

# Using json.loads()
json_str = '{"name":"Naanu","age":22,"city":"Bengaluru"}'
data1 = json.loads(json_str)
print(data1)
print(type(data))


# Writing JSON to a file in Python
# Using json.dumps() 
# The JSON package in Python has a function called json.dumps() that helps in converting a dictionary to a JSON object. It takes two parameters
data = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phone": "9976770500"
}

json_str = json.dumps(data, indent=4)
with open("sample.json", "w") as f:
    f.write(json_str)

# Using json.dump() 
# The JSON package has "dump" function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object. 
data = {
    "name": "Lowda",
    "rollno": 23,
    "cgpa": 4.6,
    "phone": "8075643218"
}

with open("sample.json", "w") as f:
    json.dump(data, f)



# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

file = open("demo.txt")
print(file.read())
file.close()

# If the file is located in a different location, you will have to specify the file path, like this
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())

with open("demo.txt") as fileR:
    for x in fileR:
        print(x)



# Python File Write
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

with open("demo.txt",'a') as writing:
    writing.write("This i wrote in the code bitch..!")

with open("demo.txt") as readF:
    print(readF.read())
                    


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

new = open("NewFile.txt",'x')

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
if os.path.exists("NewFile.txt"):
    os.remove("NewFile.txt")
else:
    print("No file exists")


