from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object initializations

coffee_machine = CoffeeMaker()
bank = MoneyMachine()
menu_options = Menu()


# function declarations

def start():
    coffee_choice_true = False
    while coffee_choice_true != True:
        coffee_lover_choice = input(
            f"Welcome to coffee machine. \nWhat would you like? {menu_options.get_items()} or report: ").lower()
        if coffee_lover_choice != "espresso" and coffee_lover_choice != "latte" and coffee_lover_choice != "cappuccino" \
                and coffee_lover_choice != "report":
            print("incorrect input: only input espresso, latte, cappuccino or report")
        else:
            coffee_choice_true = True

    if coffee_lover_choice == "report":
        coffee_machine.report()
        bank.report()
        start()
    else:
        drink = menu_options.find_drink(coffee_lover_choice)
        payment_bool = bank.make_payment(drink.cost)

        if payment_bool == True:
            resource_bool = coffee_machine.is_resource_sufficient(drink)
            if resource_bool == True:
                coffee_machine.make_coffee(drink)
                start()
            else:
                start()
        else:
            start()


# timeline

start()
