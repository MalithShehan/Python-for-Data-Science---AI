# # Read file content
# file = open("file_reading/my_file.txt", "r")
# content = file.read()
# print(content, type(content))

# # Read the file line
# file = open("file_reading/my_file.txt", "r")
# content = file.readline()
# print(content, type(content))

# # Read the file lines as list
# file = open("file_reading/my_file.txt", "r")
# content = file.readlines()
# print(content, type(content))

# # Open file for writing. Create a new file if it does not exist or truncate the file if it exists
# file = open("file_reading/my_file.txt", "w")
# content = file.readlines()
# print(content, type(content))

# # Open file for appending at the end of the file without truncating it. Create a new file if it does not exist
# file = open("file_reading/my_files.txt", "a")
# content = file.readlines()
# print(content, type(content))

# 'with' statement is used to open a file and close it automatically
# with open("file_reading/my_file.txt", "r") as file:
#     content = file.read()
#     print(content, type(content))

