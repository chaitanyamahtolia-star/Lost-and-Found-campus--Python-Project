items = []
while True:
    print("===== SMART CAMPUS LOST & FOUND =====")

    print("1. Report a Lost Item")
    print("2. Report a Found Item")
    print("3. View All Items")
    print("4. Search Items by Category")
    print("5. Run Match Checker")
    print("6. Claim an Item")
    print("7. Save and Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected: Report a Lost Item")
        name = input("Enter item name: ")
        category = input("Enter item category: ")
        Location = input("Enter item location: ")
        Contact = input("Enter your contact information: ")
        item = {
    "id": len(items) + 1,
    "name": name,
    "category": category,
    "location": Location,
    "contact": Contact,
    "status": "Open",
    "Type": "Lost"
}
        items.append(item)

    elif choice == "2":
        print("You selected: Report a Found Item")
        name = input("Enter item name: ")
        category = input("Enter item category: ")
        Location = input("Enter item location: ")
        Contact = input("Enter your contact information: ")
        item = {
    "id": len(items) + 1,
    "name": name,
    "category": category,
    "location": Location,
    "contact": Contact, 
    "status": "Open",
    "Type": "Found"
        }
        items.append(item)

    elif choice == "3":
        print("----- All Items -----")
        for item in items:
            print(f"ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Location: {item['location']} | Contact: {item['contact']} | Status: {item['status']} | Type: {item['Type']}")

    elif choice == "4":     
        print("You selected: Search Items by Category")
   
    elif choice == "5":
        print("You selected: Run Match Checker")
    
    elif choice == "6":
        print("You selected: Claim an Item")
    
    elif choice == "7":
        print("You selected: Save and Exit")
        break
 
    else:
        print("Invalid choice. Please try again.")
    


