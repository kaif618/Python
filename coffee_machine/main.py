
from machine_data import MENU, resources
from art import menu_logo, logo

def show_menu():
    print(menu_logo)
    print("📜 Drinks ----- Price")
    for drinks in MENU:
        print(f"👉 {drinks.title()}: ${MENU[drinks]['cost']}")

def money_needed():
    quarters = int(input("🪙 How many quarters: ")) * 0.25
    dimes = int(input("🪙 How many dimes: ")) * 0.10
    nickles = int(input("🪙 How many nickles: ")) * 0.05
    pennies = int(input("🪙 How many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies

def report():
    for keys in resources:
        if keys == "coffee":
            print(f"☕ {keys}: {resources[keys]}g")
        elif keys == "money":
            print(f"💰 {keys}: ${resources[keys]}")
        else:
            print(f"🥛{keys}: {resources[keys]}ml")

def machine_functionality(beverage, user_money, drink_ingredients):
    if user_money >= MENU[beverage]["cost"]:
        if resources["water"] >= MENU[beverage]["ingredients"]["water"] and resources["coffee"] >= MENU[beverage]["ingredients"]["coffee"]:
            if (beverage == "latte" or beverage == "cappuccino") and resources["milk"] >= MENU[beverage]["ingredients"]["milk"]:
                resources["milk"] -= MENU[beverage]["ingredients"]["milk"]
            resources["water"] -= MENU[beverage]["ingredients"]["water"]
            resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]
            resources["money"] += MENU[beverage]["cost"]
            print(f"🔄 Here's your ${round(user_money - MENU[beverage]['cost'], 2)} in change")
            print(f"✅ Here's Your ☕ {beverage}!! Please Enjoy 😄")
        else:
            for item in drink_ingredients:
                if drink_ingredients[item] > resources[item]:
                    print(f"❌ Not enough {item}")
    else:
        print("❌ Not enough Money!! Money refunded 💸")
        return

print(logo)
power_on = True
while power_on:
    show_menu()
    user_choice_drinks = input(f"🤖 What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice_drinks == "report":
        report()

    elif user_choice_drinks == "off":
        print("🔌 Coffee Machine powering off........")
        power_on = False

    elif user_choice_drinks == "refill":
        resources["water"] += 300
        resources["coffee"] += 100
        resources["milk"] += 200
        print("🔁 Refilled the machine, You are good to go! ☕")

    elif user_choice_drinks not in MENU:
        print("Please enter a valid drink ❌")

    else:
        print("💲 Please Insert coins")
        money = 0
        money += money_needed()

        drink_ingredients = MENU[user_choice_drinks]["ingredients"]

        machine_functionality(user_choice_drinks, money, drink_ingredients)
