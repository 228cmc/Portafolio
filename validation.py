def validate_number(prompt):
    value = input(prompt)
    if value.isdigit():
        return int(value)
    else:
        print("Invalid input. Must be a number.")
        return None

def validate_string(prompt):
    value = input(prompt).strip()
    if value != "":
        return value
    else:
        print("Invalid input. Cannot be empty.")
        return None



def validate_choice(choices, prompt):
    value = input(prompt).strip()
    if value in choices:
        return value
    else:
        print("invalid choice")
        return None
