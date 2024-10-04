# Import necessary modules
import json
import os

# Function to read data from a JSON file
def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return {}

# Function to write data to a JSON file
def write_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: {e}")

# Class to represent a simple user
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")

# Function to create a user and display their info
def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    user = User(username, email)
    user.display_info()

# Main function to run the application
def main():
    print("Welcome to the Sample Application!")
    
    # Create a user
    create_user()
    
    # Read and write data to a JSON file
    file_path = "data.json"
    data = read_data(file_path)
    print("Current data:", data)
    
    # Update data
    data['users'] = data.get('users', []) + [user.username]
    write_data(file_path, data)
    print("Data saved to", file_path)

if __name__ == "__main__":
    main()
