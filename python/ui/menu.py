import sys
from os import system


def display_menu(menu):
    """
    Display a menu where the key identifies the name of a function.
    :param menu: dictionary, key identifies a value which is a function name
    :return:
    """
    for k, function in menu.items():
        print(k, function.__name__)


def salir():
    print("Saliendo...")
    sys.exit(0)


def main():
    functions_names = [
        salir,
        probabilidad,
    ]
    menu_items = dict(enumerate(functions_names, start=0))

    while True:
        display_menu(menu_items)
        selection = int(input("Selecciona una funcion: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function
        if selection == 0:
            sys.exit(0)
        elif input("¿Quieres continuar? [y/n]: ") == "n":
            sys.exit(0)
        else:
            system("clear")


if __name__ == "__main__":
    main()
