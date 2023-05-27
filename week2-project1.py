def shoppingCart():
    shopping_list = {}

    while True:
        print()
        print('''### Shopping list ###
        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Get total
        5. Clear shopping list
        6. Quit
        ''')
        selection = input("Make your selection: ")

        if selection == "1":
            displayList(shopping_list)
        elif selection == "2":
            addItem(shopping_list)
        elif selection == "3":
            removeItem(shopping_list)
        elif selection == "4":
            getTotal(shopping_list)
        elif selection == "5":
            clearList(shopping_list)
        elif selection == "6":
            exitList(shopping_list)
            break
        else:
            print("You did not make a valid selection.")

def displayList(shopping_list):
    print()
    print("---SHOPPING LIST---")
    for item, price in shopping_list.items():
        print(f"{item}: ${price:.2f}")

def addItem(shopping_list):
    print()
    item = input("Enter the item to add to the shopping cart: ")
    price = float(input("Enter the price of the item: "))
    shopping_list[item] = price
    print(item + " has been added to the shopping cart.")

def removeItem(shopping_list):
    print()
    item = input("Enter the item to remove from the shopping cart: ")
    if item in shopping_list:
        shopping_list.pop(item)
        print(item + " has been removed from the shopping cart.")
    else:
        print(item + " is not in the shopping cart.")

def getTotal(shopping_list):
    print("Cart Total:")
    total = sum(shopping_list.values())
    print(f"${total:.2f}")

def clearList(shopping_list):
    shopping_list.clear()
    print("Shopping list is now empty.")

def exitList(shopping_list):
    print("Final Cart Total:")
    total = sum(shopping_list.values())
    print(f"${total:.2f}")

shoppingCart()
