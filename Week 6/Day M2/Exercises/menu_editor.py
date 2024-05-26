from menu_item import MenuItem
from menu_manager import MenuManager


def show_user_menu():
    print("Menu Editor")
    print("-----------")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")


def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")


def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")


def update_item_from_menu():
    name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name of the item: ")
    new_price = float(input("Enter the new price of the item: "))
    item = MenuManager.get_by_name(name)
    if item:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Error: Item not found.")


def show_restaurant_menu():
    print("Restaurant Menu")
    print("---------------")
    items = MenuManager.all_items()
    for item in items:
        print(f"{item.name}: ${item.price}")


if __name__ == "__main__":
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "V":
            name = input("Enter the name of the item to view: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name}: ${item.price}")
            else:
                print("Item not found.")

        elif choice == "A":
            add_item_to_menu()

        elif choice == "D":
            remove_item_from_menu()

        elif choice == "U":
            update_item_from_menu()

        elif choice == "S":
            show_restaurant_menu()

        elif choice == "E":
            show_restaurant_menu()
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
