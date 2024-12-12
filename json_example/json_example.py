# Read json file
with open("json_example/example_1.json", "r") as file:
    content = file.read()
    print(content, type(content))