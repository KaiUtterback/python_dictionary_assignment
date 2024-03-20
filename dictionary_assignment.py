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

'''
2. Advanced Data Handling with Python
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

# did this work
