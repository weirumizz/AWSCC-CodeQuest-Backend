import json

def main_menu():
    print("PASSWORD MANAGER")
    print("1. Add an account.")
    print("2. View all accounts.")
    print("3. Search for an account")
    print("4. Delete an account")
    print("5. Update an account")
    print("6. Quit.")

def add():
    website = input("Enter the website: ")
    email = input("Enter email: ")
    pw = input("Enter password: ")
    with open("info.json", "a") as f:
        entry = {"website": website, 
                 "email": email, 
                 "password": pw}
        json.dump(entry, f)
        f.write("\n") 
    print("Account added successfully.")

def view():
    with open("info.json", "r") as f:
        for line in f:
            entry = json.loads(line.strip())  
            if entry: 
                print("Website:", entry["website"])
                print("Email:", entry["email"])
                print("Password:", entry["password"])
                print()

def search():
    websearch = input("\nEnter the website to search: ")
    print()
    found = False
    total = 0

    with open("info.json", "r") as f:
        for line in f:
            line = line.strip() 
            if line:
                entry = json.loads(line)
                if entry["website"] == websearch:
                    found = True
                    total += 1
                    print("Website:", entry["website"])
                    print("Email:", entry["email"])
                    print("Password:", entry["password"])
                    print()

    print(f"Total of accounts found in {websearch}: {total}")

    if not found:
        print("No account found.")

def delete():
    webdelete = input("\nEnter the website to delete from: ")
    found = False
    delacc = []

    with open("info.json", "r") as f:
        data = []
        for line in f:
            entry = json.loads(line.strip())
            data.append(entry)
            if entry["website"] == webdelete:
                found = True
                delacc.append(entry)

    if not found:
        print("No accounts found.")
        return

    print(f"\nAccounts found for deletion from {webdelete}:")
    for i, entry in enumerate(delacc, start=1):
        print(f"{i}. Email: {entry['email']}, Password: {entry['password']}")
        ind = int(input("\nEnter the index of the account to delete (1, 2, ...): ")) - 1

    data.remove(delacc[ind])

    with open("info.json", "w") as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

    print(f"Account deleted successfully.")

def update():
    webupdate = input("\nEnter the website to update: ")
    found = False
    updated = []

    with open("info.json", "r") as f:
        data = []
        for index, line in enumerate(f):
            entry = json.loads(line.strip())
            data.append(entry)
            if entry["website"] == webupdate:
                found = True
                updated.append(index)

    if not found:
        print("No accounts found.")
        return

    print(f"Accounts found for updating from {webupdate}:")
    for i, index in enumerate(updated, start=1):
        print(f"{i}. Email: {data[index]['email']}, Password: {data[index]['password']}")

    choice = int(input("\nEnter the index of the account to update (1, 2, ...): ")) - 1
    updateind = updated[choice]

    new_email = input("\nEnter the new email: ")
    new_password = input("Enter the new password: ")

    data[updateind]["email"] = new_email
    data[updateind]["password"] = new_password

    with open("info.json", "w") as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

    print("Account updated successfully.")

def choice():
    again = 1
    while again == 1:
        ch = int(input("\nEnter your choice: "))
        if ch == 1:
            print("\nAdding an account: ")
            add()
        elif ch == 2:
            print("\nViewing all accounts: \n")
            view()
        elif ch == 3:
            search()
        elif ch == 4:
            delete()
        elif ch == 5:
            update()
        elif ch == 6:
            again = 0
            print("Done.")
        else:
            print("Error! Invalid input.")

main_menu()
choice()