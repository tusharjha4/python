import sys

list_length = len(sys.argv)
#print(sys.argv)

'''
if condition:
    code
'''


if list_length < 2:
    print("please pass some values")
else:
    data = sys.argv[1] # 0-filename, 1-value
    print(data)

    data_len = len(data)
    if data_len < 5:
        print("[SMALL DATA] data length is", data_len)
    else:
        print("[BIG DATA] data length is", data_len)
