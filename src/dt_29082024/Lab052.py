# Dictionary # used in JSON format for API automation
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

student1_info={
    "name":"chinnu",
    "age":5,
    "address":{
    "home_address":"AP",
    "school_address":"TG"
     }
}

print(student1_info)

student2_info={
    "name":"lucky",
    "age":2,
    "address":{
    "home_address":"KA",
    "school_address":"TD"
     }
}

student_list=[student1_info,student2_info]
print(student_list)
# Dictionary inside the dictionary is allowed.




