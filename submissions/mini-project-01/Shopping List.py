print("SHOPPING LIST")
again = 1
shop = []

while (again == 1) :
    
    print("Options: ")
    print("1. Add item to the Shopping List.")
    print("2. View Shopping List.")
    print("3. Remove item from the shopping list.")
    print("4. Quit")
    
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        a = input("Enter the item you want to add: ")
        shop.append(a)
        print(f"{a} has been adeed to your shopping list.")
    elif choice == 2:
        print(f"Your shopping list:")
        for x in shop:
            print(x)
    elif choice == 3:
        b = input("Enter the item you want to remove: ")
        if b in shop: 
            shop.remove(b)
            print(f"{b} has been removed from your shopping list.")
        else:
            print(f"Item not found!")
    elif choice == 4:
        again = 0
        print("Goodbye!")
        


