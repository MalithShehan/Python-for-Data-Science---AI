# csv.reader() method
# import csv

# with open("csv_example/customer-100.csv", "r", hewline ='') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row, type(row))    

# Writing csv data
import csv 

csv_file_path = "csv_example/sample_output.csv"

data = [
    {"Name": "John Doe", "Age": 30, "City": "New York"},
    {"Name": "Jane Doe", "Age": 25, "City": "Chicago"},
    {"Name": "Corey Schafer", "Age": 35, "City": "Boston"}
]

fieldnames = ["Name", "Age", "City"]

with open(csv_file_path, "w", newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    for row in data:
        csv_writer.writerow(row)
    print("Data written successfully")