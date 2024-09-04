import json

# List that will keep a track of records
sat_results = []

def pass_or_fail(sat_score):
    if sat_score >= 30:
        return "Pass"
    else:
        return "Fail"

# Function to check if the sat score is between the range
def valid_sat_score(sat_score):
    if sat_score >= 1.0 and sat_score <= 100.0:
        return True
    return False

# Function to validate name
def valid_name(name):
    if name.isalpha():
        return True
    return False

# Function to insert the data    
def insert_data():
    try:
        name = input("Name: ")
        if not valid_name(name.replace(" ","")):
            print("Invalid name. Name should contain only alphabetic characters.")
            return
        
        address = input("Address: ")
        city = input("City: ")
        country = input("Country: ")
        
        try:
            pincode = int(input("Pincode: "))
        except ValueError:
            print("Invalid pincode. Please enter a numeric value.")
            return
        
        try:
            sat_score = float(input("SAT score: "))
            if not valid_sat_score(sat_score):
                print("Enter a valid SAT score between 10-100%.")
                return
        except ValueError:
            print("Invalid SAT score. Please enter a numeric value.")
            return
        
        passed = pass_or_fail(sat_score)
        user_dict = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT_score": sat_score,
            "Passed": passed
        }
        
        sat_results.append(user_dict)
        print("Data inserted successfully!")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to view the data  
def view_all_data():
    if not sat_results:
        print("No data available")
        return
    print(json.dumps(sorted(sat_results, key=lambda x: x['SAT_score'], reverse=True), indent=4))

# Function to get the rank depending on the sat_score   
def get_rank():
    username = input("Enter the name of the person to get the rank details: ").lower()
    sorted_results = sorted(sat_results, key=lambda x: x['SAT_score'], reverse=True)
    
    for rank, results in enumerate(sorted_results, start=1):
        if results['Name'].lower() == username:
            print(f"{username}'s rank details: {rank}")
            return
    print(f"Record with the name {username} was not found")

# Function to update the score  
def update_score():
    username = input("Enter the name to update the SAT score: ").lower()
    for user in sat_results:
        if user['Name'].lower() == username:
            try:
                updated_score = float(input("Enter the updated SAT score: "))
                if not valid_sat_score(updated_score):
                    print("Enter a valid SAT score between 10-100%.")
                    return
                user['SAT_score'] = updated_score
                user['Passed'] = pass_or_fail(updated_score)
                print("Score updated successfully!")
            except ValueError:
                print("Invalid SAT score. Please enter a numeric value.")
            return
    print(f"Record with the name {username} was not found")

# Function to delete the record  
def delete_record():
    username = input("Enter the name to delete the record: ").lower()
    for user in sat_results:
        if user['Name'].lower() == username:
            sat_results.remove(user)
            print("Record deleted successfully!")
            return
    print(f"Record with name {username} not found.")
    
# Function to calculate the average SAT score
def calculate_average_sat_score():
    if not sat_results:
        print("No data available to calculate average.")
        return
    total_score = 0
    for user in sat_results:
        total_score += user['SAT_score']
    average = total_score / len(sat_results)
    print(f"The average SAT score is: {average:.2f}")

# Function to filter the records by pass or fail    
def filter_by_status():
    status = input("Enter the status to filter by (Pass/Fail): ").capitalize()
    filtered = [result for result in sat_results if result['Passed'] == status]
    if not filtered:
        print(f"No records found with status {status}")
        return
    print(json.dumps(filtered, indent=4))

# Function to save data to JSON file  
def save_to_json_file():
    with open('sat_results.json', 'w') as file:
        json.dump(sat_results, file, indent=4)
    print("Data saved to sat_results.json file...")
    
# Main Menu
def menu():
    while True:
        print("Menu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Save data to JSON file")
        print("9. Exit")
        
        choice = input("Select an option (1-9): ")
        
        if choice == '1':
            insert_data()
        elif choice == '2':
            view_all_data()
        elif choice == '3':
            get_rank()
        elif choice == '4':
            update_score()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            calculate_average_sat_score()
        elif choice == '7':
            filter_by_status()
        elif choice == '8':
            save_to_json_file()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
