
from dbHelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("1. Insert User")
        print("2. Fetch All Users") 
        print("3. Delete User")
        print("4. Update User")
        print("5. Exit")
        print()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                #Insert user
                id = int(input("Enter user ID: "))
                name = input("Enter user name: ")
                phNumber = input("Enter phone number: ")
                db.insert_user(id, name, phNumber)
            elif choice == 2:
                # Display all users
                db.fetch_all()
            elif choice == 3:
                #delete user
                id = int(input("Enter user ID to delete: "))
                db.delete_user(id)         
            elif choice == 4:
                #update user
                id = int(input("Enter user ID to update: "))
                name = input("Enter new user name: ")
                phNumber = input("Enter new phone number: ")
                db.update_user(id, name, phNumber)
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
        except Exception as e:
            print(f"Error: {e}. Please try again.")
            
if __name__ == "__main__":
    main()

        