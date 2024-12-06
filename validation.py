def validate_number(prompt):
    """ this method evaluates a given argument if its a string or not with the method isdigit.
     it takes a prompt and returns the  integer value if it's correct   otherwise it is in an eternal  """

    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return None

        if value.isdigit():
            return int(value)
        else:
            print("invalid, it must be number")

def validate_string(prompt):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return None
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("invalid, it's empty")



def validate_choice(choices, prompt):
    """
    validates a choice from an iterable in this case a list
    """
    print('choices',choices)
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return None
        value = input(prompt).strip()
        if value in choices:
            return value
            print(f'changed to {value}')
        else:
            print("invalid choice")
