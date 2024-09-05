# Dictionary
# key and value

student_info={
    "name":"vish",
    "age":30,
    "age":30,  # if duplicates are there it will ignore
    "address":"hyd"
     }

student_info={
    "name":"vish",
    "age":30,
    "age":45,  # if 2 keys are same it will take latest one and ignore previous one. Here it is 45
    "address":"hyd"
     }

print(student_info) # {'name': 'vish', 'age': 45, 'address': 'hyd'}
print(student_info["name"])
print(student_info["age"])

# keys will be unique

# we can change the values in the dictionary

student_info["name"]="lucky"
print(student_info) # {'name': 'lucky', 'age': 45, 'address': 'hyd'}

# Another way of creating a dictionary- But its better to avoid this way

student_info=dict(name="ram",age=20,address="KA")
print(student_info)

print("------------------------------------")

# Dictionary is an unordered collection of data.

student_info={
    "name":"chinnu",
    "age":5,
    "address":{
    "home_address":"AP",
    "school_address":"TG"
     }
}

print(student_info)

# Dictionary inside the dictionary is allowed.

