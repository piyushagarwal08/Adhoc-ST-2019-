file_name = input('Enter the file name: ')
file_handle = open(file_name)
line = file_handle.readlines()
print("No of lines : ",len(line))
