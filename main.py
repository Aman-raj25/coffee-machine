# Import necessary classes from other files
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the MoneyMachine and CoffeeMaker classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Create an instance of the Menu class
menu = Menu()

# Initialize the machine state (on/off)
is_on = True

# Main loop for interacting with the coffee machine
while is_on:
    # Get the available drink options from the menu
    options = menu.get_items()

    # Ask the user for their choice
    choice = input(f"What would you like? ({options}): ")

    # Check user input
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Generate and display a report of resources
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the selected drink from the menu
        drink = menu.find_drink(choice)

        # Check if there are enough resources and process payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the selected coffee
            coffee_maker.make_coffee(drink)
