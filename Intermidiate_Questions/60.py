import json

# Step 1: Read data from a JSON file
file_path = "data.json"
try:
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load JSON data as a Python dictionary
    print("Original JSON data:")
    print(data)

    # Step 2: Modify a value
    key_to_modify = input("Enter the key to modify: ")
    if key_to_modify in data:
        new_value = input(f"Enter the new value for '{key_to_modify}': ")
        data[key_to_modify] = new_value
    else:
        print(f"Key '{key_to_modify}' not found in the JSON file.")

    # Step 3: Write updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)  # Write JSON data with indentation for readability

    print("Updated JSON data written to the file.")

except FileNotFoundError:
    print("Error: JSON file not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please ensure the file is properly formatted.")
