''' Real-World Python Dictionary Applications
The aim of this assignment is to reinforce your understanding and application of Python dictioanries, nested colelctions, and
dictionary methods in real world scenarios.
You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. 
Your task is to update this menu based on given instructions. 
This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

Problem Statement:
Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

TASKS: 
- Add a new category called "Beverages" with at least two items.
- Update the price of "Steak" to 17.99.
- Remove "Bruschetta" from "Starters".
'''

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_to_menu(restaurant_menu, category):
    if category not in restaurant_menu:
        restaurant_menu[category] = []
        print(f"new category {category} added to menu!")
    else:
        print(f"Category {category} already exists on our menu!")
        
def add_item(restaurant_menu, category, item):
    if item not in category:
            restaurant_menu[category].append(item)
            print(f"New item {item} added to {category}.")
    else:
        print(f"The item {item} already exists in {category}!")

def remove_item(restaurant_menu, category, item):
    if category in restaurant_menu and item in restaurant_menu[category]:
        del restaurant_menu[category][item]
        print(f"{item} removed from {category} on the menu")
    else:
        print(f"{item} already not on menu")

def update_price(category, item, value, cost):
    if item in category:
        category[item][value] = cost
        print(f"{item} price updated to {cost}")
    else:
        print(f"{item} not found on menu")

def display_menu(restaurant_menu):
    print("Menu")
    for category, item in restaurant_menu.items():
        print(f"{category}: {item}")

# adds a new category to the menu
add_to_menu(restaurant_menu, 'Beverages')
# adds a new item to the category of your choice in the menu
add_item(restaurant_menu, 'Beverages', 'Water')
add_item(restaurant_menu, 'Beverages', 'Coke Products')
# removes item from menu
remove_item(restaurant_menu, 'Starters', 'Bruschetta')
# updates the price of different items
update_price(restaurant_menu, 'Main Course', 'Steak', 17.99)
# displays current menu
print()
display_menu(restaurant_menu)
print()

'''  2. Advanced Data Handling with Python

Objective:
The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. 
You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Develop a program that:
Manages room bookings, where each room has details such as booking status (booked/available) and customer name.

Implement functions to:
- Book a room (mark as booked and assign to a customer).
- Check-out a customer (mark room as available and remove customer name).
- Display the status of all rooms.
- Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
'''

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(hotel_rooms, room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

def check_out_customer(hotel_rooms, room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"{customer_name} has checked out of room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

def display_room_status(hotel_rooms):
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status']}, Customer: {details['customer']}")


# Initial hotel room structure
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}


book_room(hotel_rooms, "101", "Alice")

check_out_customer(hotel_rooms, "102")

display_room_status(hotel_rooms)
print()


'''  Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

Problem Statement:

Create a system that:
- Holds a dictionary of products where each product has attributes like name, category, and price.
- Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
- Handle cases where no matches are found.
'''

def search_products(products, query):

    results = []
    query = query.lower()  
    for product_id, product_details in products.items():
        if query in product_details["name"].lower():
            results.append((product_id, product_details))
    return results

def run_search():
    products = {
        "1": {"name": "Laptop", "category": "Electronics", "price": 800},
        "2": {"name": "Shirt", "category": "Clothing", "price": 20}
    }
    
    while True:
        query = input("Enter the product name to search (or 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting search.")
            break
        
        search_results = search_products(products, query)

        if search_results:
            print("Search Results:")
            for product_id, product_details in search_results:
                print(f"Product ID: {product_id}, Name: {product_details['name']}, Category: {product_details['category']}, Price: {product_details['price']}")
        else:
            print("No matching products found.")

run_search()

'''  3. Python Programming Challenges for Customer Service Data Handling

Objective:
This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. 
You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Develop a program that:
- Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

Implement functions to:
- Open a new service ticket.
- Update the status of an existing ticket.
- Display all tickets or filter by status.
- Initialize with some sample tickets and include functionality for additional ticket entry.

'''
def open_ticket(ticket_tracker):
    ticket_id = input("Enter ticket ID: ")
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    status = "open"  

    ticket_tracker[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": status}

def update_status(ticket_tracker):
    ticket_id = input("Enter ticket ID to update: ")
    new_status = input("Enter new status (open/closed): ")

    if ticket_id in ticket_tracker:
        ticket_tracker[ticket_id]["Status"] = new_status
        print("Ticket status updated successfully.")
    else:
        print("Ticket ID not found.")

def display_tickets(ticket_tracker):
    print("All Tickets:")
    for ticket_id, ticket_details in ticket_tracker.items():
        print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}, Status: {ticket_details['Status']}")


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def run_ticket_program():
    while True:
        print("\n1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            open_ticket(service_tickets)
        elif choice == "2":
            update_status(service_tickets)
        elif choice == "3":
            display_tickets(service_tickets)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

run_ticket_program()

'''  4. Python Essentials for Business Analytics
Objective:
This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. 
You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

Task 1: Sales Data Cloning and Modification
Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

Problem Statement:
You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales figures for a specific week.

Given Sales Data:

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

- Create a deep copy of weekly_sales.
- Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.
'''
import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}


copied_sales = copy.deepcopy(weekly_sales)
copied_sales["Week 2"]["Electronics"] = 18000


print("Original Sales Data:")
print(weekly_sales)
print("\nCopied Sales Data with Updated Electronics Sales in Week 2:")
print(copied_sales)
