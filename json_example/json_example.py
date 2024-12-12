# Read json file data
# import json

# josn_file_path = "json_example/example_1.json"

# with open(josn_file_path, "r") as file:
#     data = json.load(file)
#     print(data, type(data))

# Creat json file & write json file data
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

json_file_path = "json_example/example_3.json"

with open(json_file_path, "w") as json_file:
    json_data= json.dumps(data, indent = 4)
    json_file.write(json_data)
    print(json_file, type(json_file))
    