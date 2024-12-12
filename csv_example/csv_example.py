# csv.reader() method
# import csv

# with open("csv_example/customer-100.csv", "r", hewline ='') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row, type(row))    

# Writing csv data
# import csv 

# csv_file_path = "csv_example/sample_output.csv"

# data = [
#     {"Name": "John Doe", "Age": 30, "City": "New York"},
#     {"Name": "Jane Doe", "Age": 25, "City": "Chicago"},
#     {"Name": "Corey Schafer", "Age": 35, "City": "Boston"}
# ]

# fieldnames = ["Name", "Age", "City"]

# with open(csv_file_path, "w", newline='') as file:
#     csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     for row in data:
#         csv_writer.writerow(row)
#     print("Data written successfully")

# your are task with a  create a python program to manage a company emplyee records stored in csv file. the programe  should read the emplyee details from a csv file filter the record based on a condition and write the filterd records to a new csv file 
# 01. files provided : 
# input files : emplyees.csv
# contains the following fields
#  * EmployeeId
#  * Name
#  * DepartmentSalary
# 02. Example content
# high_salary_employee.csv
# you will create  this file it should contain records of employee who salary above 60,000,field should remain the same 

#         1,John,IT,60000
#         2,Jane,HR,55000
#         3,Mike,Finance,70000
#         4,Linda,IT,75000

# Task: 
# * Read the input files 
# * You csv.reader to read employee.csv & display all the records. 
# * filter the records -  identify employee with the salary greater than 50000 
# * write the filter records : use csv.diwriter use to new file name high_salary_employee

import csv

# File paths
input_file = "csv_example/employees.csv"
output_file = "csv_example/high_salary_employee.csv"

# Define the salary threshold
salary_threshold = 60000

def read_and_display_employees(file_path):
    """Reads and displays all records from the input CSV file."""
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            print("Employee Records:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

def filter_and_write_employees(input_path, output_path, threshold):
    """Filters employees with a salary above the threshold and writes them to a new CSV file."""
    try:
        with open(input_path, mode='r') as infile, open(output_path, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Read the header and write it to the output file
            header = next(reader, None)
            if header:
                writer.writerow(header)

            # Process and filter rows
            for row in reader:
                try:
                    employee_id, name, department, salary = row
                    salary = float(salary)  # Convert salary to float for comparison
                    if salary > threshold:
                        writer.writerow(row)  # Write filtered row to the new file
                except ValueError:
                    print(f"Skipping invalid row: {row}")

            print(f"Filtered employees written to {output_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")

# Main execution
read_and_display_employees(input_file)
filter_and_write_employees(input_file, output_file, salary_threshold)