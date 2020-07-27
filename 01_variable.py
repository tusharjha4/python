
# String example
name = "nirmal"
print(name.capitalize())
print(len(name))
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.isalnum())

print(3 * name)
print(name + name)
#print(name - name) doesn't works in string
#print(name % name) doesn't works in string
#print(name / name) doesn't works in string


#integer example
age = 10

print(age + age)
print(age - age)
print(age * age)
print(age / age)
print(age % age)
#print(len(age)) doesn't works in int


#boolean example
isIndian = True # 0 - False, 1 - True
print(type(isIndian))
print(isIndian + isIndian)
print(isIndian - isIndian)
print(isIndian / isIndian)
print(isIndian % isIndian)
print(isIndian * isIndian)
#print(len(isIndian)) doesn't works in boolean


#float example
height = 5.8
print(height + height)
print(height - height)
print(height * height)
print(height / height)
print(height % height)
#print(len(height)) doesn't works in float


name = "tushar"
for char in name:
    print(char)


x = 100
y = 200

x, y = y, x
print("x is", x)
print("y is", y)


a, b, c = 100, 200, "tushar"  #value unpacking
print("a is", a)
print("b is", b)
print("c is", c)
