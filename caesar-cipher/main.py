# caesar-cipher/main.py
# Uses caesar cipher to encrypt/decipher a message.

# Imports
import string

# Constants
ALPHABET = list(string.ascii_lowercase)
LOGO = '''
   █████████                                                
  ███▒▒▒▒▒███                                               
 ███     ▒▒▒   ██████    ██████   █████   ██████   ████████ 
▒███          ▒▒▒▒▒███  ███▒▒███ ███▒▒   ▒▒▒▒▒███ ▒▒███▒▒███
▒███           ███████ ▒███████ ▒▒█████   ███████  ▒███ ▒▒▒ 
▒▒███     ███ ███▒▒███ ▒███▒▒▒   ▒▒▒▒███ ███▒▒███  ▒███     
 ▒▒█████████ ▒▒████████▒▒██████  ██████ ▒▒████████ █████    
  ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒     

   █████████   ███            █████                         
  ███▒▒▒▒▒███ ▒▒▒            ▒▒███                          
 ███     ▒▒▒  ████  ████████  ▒███████    ██████  ████████  
▒███         ▒▒███ ▒▒███▒▒███ ▒███▒▒███  ███▒▒███▒▒███▒▒███ 
▒███          ▒███  ▒███ ▒███ ▒███ ▒███ ▒███████  ▒███ ▒▒▒  
▒▒███     ███ ▒███  ▒███ ▒███ ▒███ ▒███ ▒███▒▒▒   ▒███      
 ▒▒█████████  █████ ▒███████  ████ █████▒▒██████  █████     
  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒███▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒      
                    ▒███                                    
                    █████                                   
                   ▒▒▒▒▒                                    
'''

# Functions
def main() -> None:
    print(LOGO)

    while True:
        message = input(f"Message: ").lower()
        shift = verify_input("Shift: ", "int")
        action = verify_input("Would you like to encrypt or decipher? ", "list", ["e", "d"]) 

        if action == "d":
            shift *= -1

        print(f"Your new message is: {caesar(message, shift)}")

        redo = verify_input("Would you like to try again? ", "list", ["y", "n"])

        if redo == "n":
            break

def caesar(arg_message: str, arg_shift: int) -> str:
    new_message = ""
    for char in arg_message:
        if char not in ALPHABET:
            new_message += char

        else:
            current_index = ALPHABET.index(char)
            new_index = (current_index + arg_shift) % len(ALPHABET)
            new_message += ALPHABET[new_index]

    return new_message

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

# Execute
main()
