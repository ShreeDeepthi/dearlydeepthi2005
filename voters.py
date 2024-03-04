voters_data = [
    {"name": "John", "id": "001", "age": 25, "address": "123 Main St", "citizenship": "US"},
    {"name": "Alice", "id": "002", "age": 30, "address": "456 Oak St", "citizenship": "CA"},
    {"name": "Bob", "id": "003", "age": 18, "address": "789 Pine St", "citizenship": "UK"},
    # Add more voters as needed
]

with open("voters_data.txt", "w") as file:
    for voter in voters_data:
        file.write(f"{voter['name']} {voter['id']} {voter['age']} {voter['address']} {voter['citizenship']}\n")

# Reading the file
with open("voters_data.txt", "r") as file:
    voter_records = file.readlines()

# Creating a dictionary for quick lookup
voter_dict = {record.split()[1]: {"age": int(record.split()[2]), "citizenship": record.split()[4]} for record in voter_records}

# Asking for ID and age
user_id = input("Enter your ID: ")
user_age = int(input("Enter your age: "))

# Checking age and citizenship using the dictionary
if user_id in voter_dict:
    if user_age < voter_dict[user_id]["age"]:
        print("Invalid age.")
    elif voter_dict[user_id]["citizenship"] != "US":
        print("Invalid citizenship.")
    else:
        print("Valid voter.")
else:
    print("Invalid ID.")