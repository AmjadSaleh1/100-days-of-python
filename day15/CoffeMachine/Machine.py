from Data import MENU
from Data import resources

Turn_machine = True


def is_transaction_succesful(money_r, drink_cost):
    """return true if the payment accepted"""
    if money_r >= drink_cost:
        change = round(money_r - drink_cost, 2)
        print(f"here is the ${change}")
        resources["Money"] += drink_cost
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.”")
        return False


def make_coffe(drink_name, oder_ing):
    """deduct the required inge from the resources"""
    for item in oder_ing:
        resources[item] -= oder_ing[item]
    print(f"here is youre {drink_name}☕")


def coin_procsses():
    """return calculated money that been inserted"""
    print("please Insert coins")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return money


def print_report():
    """print report"""
    print("the current resources values :")
    for key in resources:
        print(f"{key}: {resources[key]} ")


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


while Turn_machine:
    choose = input(" “What would you like? (espresso/latte/cappuccino):” ").lower()
    if choose == "report":
        print_report()
    else:
        if not check_resources(MENU[choose]["ingredients"]):
            Turn_machine = False
        else:
            money_inserted = coin_procsses()
            if is_transaction_succesful(money_inserted, MENU[choose]["cost"]):
                make_coffe(choose, MENU[choose]["ingredients"])

print_report()
check_resources(MENU["espresso"]["ingredients"])
