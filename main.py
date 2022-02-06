from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_is_on = True
while machine_is_on:
    print(menu.get_items())
    user_choice = input("What would you like?: ").lower()

    if user_choice == "off":
        machine_is_on = False

    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        chosen_drink = menu.find_drink(user_choice)

        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)
