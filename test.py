def shoppingCart():
    while True:
        print()
        print('''### Shopping list ###
        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Get total
        5. Clear shopping list
        6. quit
        ''')
        selection = input ("Make your selection: ")

        if selection == "1":
            displayList()
        if selection == "2":
            addItem()
        if selection == "3":
            removeItem()
        if selection == "4":
            getTotal()
        if selection == "5":
            clearList()
        if selection == "6":
            exitList()
        else:
            print("You did not make a valid selection.")
shopping_list = {}


def displayList():
    print()
    print("---SHOPPING LIST---")
    for n in shopping_list:
        print(n)

def addItem():
    print()
    item = input("Enter the item to the shopping cart: ")
    price = float(input("what's the price of the item: "))
    shopping_list[item]=price
    print(item + " been added")

def removeItem():
    print()
    item = input("item was removed from shopping cart: ")
    shopping_list.pop(item)
    print(item + " been removed")

def getTotal():
    print("Cart Total:")
    print(sum(shopping_list.values()))

def clearList():
    shopping_list.clear()
    print("Shopping list now empty")
                  
def exitList():
    print("Cart Total:")
    print(sum(shopping_list.values()))
shoppingCart()
