def validate_number(prompt):
    value = input(prompt)
    if value.isdigit():
        return int(value)
    else:
        print("invalid, it must be number")
        return None

def validate_string(prompt):
    value = input(prompt).strip()
    if value != "":
        return value
    else:
        print("invalid, it's empty")
        return None



def validate_choice(choices, prompt):
    """
    validates a choice from an iterable in this case a list
    """
    print('choices',choices)
    value = input(prompt).strip()
    if value in choices:
        return value
        print(f'changed to {value}')
    else:
        print("invalid choice")
        return None
