# calculator/main.py

# Constants
LOGO = '''
 ▄████████    ▄████████  ▄█        ▄████████ ███    █▄   ▄█          ▄████████     ███      ▄██████▄     ▄████████ 
███    ███   ███    ███ ███       ███    ███ ███    ███ ███         ███    ███ ▀█████████▄ ███    ███   ███    ███ 
███    █▀    ███    ███ ███       ███    █▀  ███    ███ ███         ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
███          ███    ███ ███       ███        ███    ███ ███         ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
███        ▀███████████ ███       ███        ███    ███ ███       ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
███    █▄    ███    ███ ███       ███    █▄  ███    ███ ███         ███    ███     ███     ███    ███ ▀███████████ 
███    ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███▌    ▄   ███    ███     ███     ███    ███   ███    ███ 
████████▀    ███    █▀  █████▄▄██ ████████▀  ████████▀  █████▄▄██   ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
                        ▀                               ▀                                               ███    ███ 
'''

# Functions
def main() -> None:
    functions = {
        "+": add,
        "*": multiply,
        "-": subtract,
        "/": divide,
    }
    redo = ""
    
    print(LOGO)

    while True:
        if redo == "":
            number1 = verify_input("Number 1: ", "float")
        
        else:
            number1 = result
        
        operator = verify_input("Operator: ", "list", ["+", "*", "-", "/"])
        number2 = verify_input("Number 2: ", "float")
        operation = functions[operator]
        result = operation(number1, number2)

        print(f"{number1} {operator} {number2} = {result}")

        redo = verify_input(f"Would you like to use {result} as Number 1 and keep using the calculator? ", "list", ["y", "n"])

        if redo == "n":
            break

def add(n1, n2) -> float:
    return n1 + n2

def multiply(n1, n2) -> float:
    return n1 * n2

def subtract(n1, n2) -> float:
    return n1 - n2

def divide(n1, n2) -> float:
    if n2 == 0:
        return n1

    return n1 / n2

def verify_input(arg_text: str, arg_type: str, arg_options: list = None):
    if arg_type == "list":
        response = input(f"{arg_text} {arg_options}: ").lower()
        while response not in arg_options:        
            response = input(f"Please, select a valid response {arg_options}: ").lower()

        return response

    elif arg_type == "float":
        while True:
            try:
                response = float(input(f"{arg_text}"))
                return response

            except ValueError:
                print("Error: Please, type a valid number.")

# Execute
main()