import string

def evaluate_password():
    special_chars = string.punctuation

    while True:
        PSW = input("Enter your password: ")
        length = 9 <= len(PSW) <= 12
        has_upper = any(char.isupper() for char in PSW)
        has_lower = any(char.islower() for char in PSW)
        has_digit = any(char.isdigit() for char in PSW)
        has_special = any(char in special_chars for char in PSW)

        if length and has_upper and has_lower and has_digit and has_special:
            print("Strong password!")
            break  # Exit the loop if the password is strong
        else:
            print("Weak password! It must have at least:")
            if not length:
                print("- Between 9 to 12 characters")
            if not has_upper:
                print("- An uppercase letter")
            if not has_lower:
                print("- A lowercase letter")
            if not has_digit:
                print("- A digit")
            if not has_special:
                print("- A special character")
            print("Try again!\n")


evaluate_password()
