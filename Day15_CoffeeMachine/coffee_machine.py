MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many dimes? :")) * 0.10
    total += int(input("How many nickles? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drinkname, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drinkname} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}ml")
       print(f"Money: ${profit}g")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
                payment = process_coin()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink['ingredients'])
