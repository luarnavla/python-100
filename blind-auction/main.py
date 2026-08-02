# blind-auction/main.py
# Uses dictionaries to make blind bids.

# Imports
import os

# Constants
LOGO = '''
$$$$$$$\  $$\       $$$$$$\ $$\   $$\ $$$$$$$\                     
$$  __$$\ $$ |      \_$$  _|$$$\  $$ |$$  __$$\                    
$$ |  $$ |$$ |        $$ |  $$$$\ $$ |$$ |  $$ |                   
$$$$$$$\ |$$ |        $$ |  $$ $$\$$ |$$ |  $$ |                   
$$  __$$\ $$ |        $$ |  $$ \$$$$ |$$ |  $$ |                   
$$ |  $$ |$$ |        $$ |  $$ |\$$$ |$$ |  $$ |                   
$$$$$$$  |$$$$$$$$\ $$$$$$\ $$ | \$$ |$$$$$$$  |                   
\_______/ \________|\______|\__|  \__|\_______/                    

 $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |  $$ |$$  __$$\\__$$  __|\_$$  _|$$  __$$\ $$$\  $$ |
$$ /  $$ |$$ |  $$ |$$ /  \__|  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |
$$$$$$$$ |$$ |  $$ |$$ |        $$ |     $$ |  $$ |  $$ |$$ $$\$$ |
$$  __$$ |$$ |  $$ |$$ |        $$ |     $$ |  $$ |  $$ |$$ \$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$\   $$ |     $$ |  $$ |  $$ |$$ |\$$$ |
$$ |  $$ |\$$$$$$  |\$$$$$$  |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |
\__|  \__| \______/  \______/   \__|   \______| \______/ \__|  \__|
'''

# Functions
def main() -> None:
    print(LOGO)

    while True:
        bidders = {}
        number_bidders = verify_input("How many bidders there? ", "int")
        biggest_bidder = ""
        biggest_bid = 0

        for bidder in range(number_bidders):
            key, value = add_bid()
            bidders[key] = value

            if value > biggest_bid:
                biggest_bidder = key
                biggest_bid = value

            os.system('cls' if os.name == 'nt' else 'clear')

        print(f"The winner is {biggest_bidder} with a bid of ${biggest_bid}")

        redo = verify_input("Would you like to try again? ", "list", ["y", "n"])

        if redo == "n":
            break

def add_bid() -> tuple:
    key = input("Name: ")
    value = verify_input("Bid: $", "float")
    return key, value

def verify_input(arg_text: str, arg_type: str, arg_options: list = None):
    if arg_type == "list":
        response = input(f"{arg_text} {arg_options}: ").lower()
        while response not in arg_options:        
            response = input(f"Please, select a valid response {arg_options}: ").lower()

        return response

    elif arg_type == "int":
        while True:
            try:
                response = int(input(f"{arg_text}"))
                return response

            except ValueError:
                print("Error: Please, type a valid number.")

    elif arg_type == "float":
        while True:
            try:
                response = float(input(f"{arg_text}"))
                return response

            except ValueError:
                print("Error: Please, type a valid number.")

# Execute
main()
