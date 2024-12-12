# Read json file data
# import json

# josn_file_path = "json_example/example_1.json"

# with open(josn_file_path, "r") as file:
#     data = json.load(file)
#     print(data, type(data))


# Creat json file & write json file data
# import json

# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }

# json_file_path = "json_example/example_3.json"

# with open(json_file_path, "w") as json_file:
#     json_data= json.dumps(data, indent = 4)
#     json_file.write(json_data)
#     print(json_file, type(json_file))
    

# Student.json which contains information about students and their grades. Your task is to 
# 01. Read the json file.
# 02. Display the name of all students who scored above 75.
# 03. Add a new student record to the file.
# 04. Save the updated data back to the json file.
# 05. Exit the program.

# import json

# def read_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# def display_students_above_75(data):
#     for student in data:
#         if student['grade'] > 75:
#             print(student['name'])
            
# def add_new_student(data, name, grade):
#     new_student = {
#         'name': name,
#         'grade': grade
#     }
#     data.append(new_student)
# def save_to_json_file(file_path, data):
#     with open(file_path, 'w') as file:
#         json_data = json.dumps(data, indent=4)
#         file.write(json_data)

# def main():
#     json_file_path = 'json_example/students.json'
#     data = read_json_file(json_file_path)
#     add_new_student(data, 'Bool Doe', 80)
#     save_to_json_file(json_file_path, data)
#     display_students_above_75(data)
    
# if __name__ == '__main__':
#     main()



