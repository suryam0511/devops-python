

import requests
import json

# Function to call the API
def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


# Function to process data
def process_users(users):
    processed_data = []

    for user in users:
        user_info = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "company": user["company"]["name"]
        }
        processed_data.append(user_info)

    return processed_data


# Function to save data to JSON file
def save_to_file(data):
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)


# Main function
def main():
    users = fetch_users()
    processed_users = process_users(users)

    print("\n--- User Data ---")
    for user in processed_users:
        print(user)

    save_to_file(processed_users)
    print("\nData saved to output.json")


main()
