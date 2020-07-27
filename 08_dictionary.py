'''
name
email
roll number
age

[name, email, roll_number, age]
["tushar", "abc@gmail.com", 123, 25]
["tushar", 123, 25]

{
   "name" : "tushar",
   "age" : 25,
   "email": "abc@gmail.com",
   "roll_number": 123
}

'''


student_dict = {}
print(type(student_dict))
student_dict["name"] = "tushar"
student_dict["age"] = 25
student_dict["email"] = "abc@gmail.com"
student_dict["roll_number"] = 123

'''
print(student_dict)
print("name is ", student_dict.get("name"))
print("age is ", student_dict.get("age"))
print("roll number is ", student_dict.get("roll_number"))
print("email is ", student_dict.get("email1"))

print(len(student_dict))

print(student_dict.keys())
print(student_dict.values())


for key, value in student_dict.items():
    print("key is ", key, " value is ", value)

'''


name = input("enter your name: ")
age = input("enter your age: ")
roll_number = input("enter your roll number: ")
email = input("enter your email: ")

student_data = {}
student_data["email"] = email
student_data["name"] = name
student_data["roll_number"] = roll_number
student_data["age"] = age
print(student_data)


student_data_list = []
student_data_list.append(student_dict)
student_data_list.append(student_data)

print(student_data_list)
