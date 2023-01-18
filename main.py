import data
from data import MENU
from data import resources


def check(ch):
    """"Resource check"""
    enough = True
    for i in ch:
        if ch[i] >= resources[i]:
            print(f"Sorry there is not enough {i} ")
            enough = False
    return enough


def paying():
    """"Calculation of the amount paid"""
    total = int(input("How many  quarters you have? ")) * 0.25
    total += int(input("How many  dimes you have? ")) * 0.1
    total += int(input("How many  nickles you have? ")) * 0.05
    total += int(input("How many   pennies you have? ")) * 0.01
    return total


def succeeded(customer_money, drink_price):
    if customer_money >= drink_price:
        residual = round(customer_money - drink_price, 2)
        print(f"Here is ${residual} dollars in change")
        data.profet += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

        return False


def makecoffee(name, ingra):
    for i in ingra:
        resources[i] -= ingra[i]
    print(f"“Here is your {name}. Enjoy")


# TODO 2. Check the user’s input to decide what to do next.
flag = True

while flag:
    # TODO 1. User input “What would you like? (espresso/latte/cappuccino):”

    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        flag = False

    elif choice == "report":

        print(
            f" water : {resources['water']} \n milk : {resources['milk']} \n coffee : {resources['coffee']} \n Mony :{data.profet}")

    else:
        info = MENU[choice]
        if check(info["ingredients"]):
            p = paying()
            if succeeded(p, info["cost"]):
                makecoffee(choice, info["ingredients"])
