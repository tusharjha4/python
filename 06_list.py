
data_list = []
print(type(data_list))

data_list.append(10)
data_list.append(11)
data_list.append("tushar")
data_list.append(True)
data_list.append(400.4)
print(data_list)
#print(len(data_list))
#data_list.clear()

print(data_list)
data_list.remove(10)
print(data_list)

return_value = data_list.pop(1)
print(return_value)
print(data_list)

data_list.reverse()
print(data_list)

data_list.sort()
print(data_list)

data_list.sort(reverse=True)
print(data_list)


for value in data_list:
    print(value)


