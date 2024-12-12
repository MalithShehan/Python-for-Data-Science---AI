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

# How to write to a file in Python
# with open("file_reading/my_file.txt", "w") as file:
#     file.write("This is owesome\n")
#     file.write("Programming is fun")

# # Wirtelines method
# with open("file_reading/my_file.txt", "w") as file:
#     file.writelines(["This is owesome\n", "Programming is fun\n", "Python is the best\n"])

# Exercise 01. Create a program that reads the content of a file and display it on the console
# Create a program that storage and manage contacts in a file name contacts.txt. 
# 01. Each contact should have a name, a phone number and email. 
# 02. Feature to implement view all contact read and display all contacts on the file. 
# 03. Add the new contact: apend to the contact file. 
# 04. Exite on the program.
# John Doe, 12345678, john@example.com
# Kate Fery, 87654321, kate@example.com

def add_contact(name, phone, email):
    with open("file_reading/contacts.txt", "a") as file:
        file.write(f"{name}, {phone}, {email}\n")
        print(f"Contact {name} added successfully")

def view_contacts():
    with open("file_reading/contacts.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact)

def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()