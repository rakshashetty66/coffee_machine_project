Menu = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 200
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    """Checks if enough resources are available for the coffee order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Calculates the total amount of money inserted by the user."""
    print("Please insert coins.")
    total = 0
    try:
        coins_five = int(input("How many 5rs coins?: "))
        coins_ten = int(input("How many 10rs coins?: "))
        coins_twenty = int(input("How many 20rs coins?: "))
        total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
    except ValueError:
        print("Invalid input! Please enter integer values.")
        return 0
    return total


def is_payment_successful(money_received, coffee_cost):
    """Checks if payment is sufficient, returns change if overpaid, refunds if underpaid."""
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        if change > 0:
            print(f"Here is Rs. {change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, coffee_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    elif choice in Menu:
        coffee_type = Menu[choice]
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if payment > 0 and is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
    else:
        print("Invalid choice. Please select a valid option.")
