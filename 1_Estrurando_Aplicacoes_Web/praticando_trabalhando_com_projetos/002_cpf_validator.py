def number_validation(user_input):
    return user_input.isdigit()


def character_validation(user_input):
    return len(user_input) == 11


def formated_response(user_input):
    if not number_validation(user_input):
        return "ERROR: CPF must be a only valid number."

    if not character_validation(user_input):
        return "ERROR: The CPF must contain 11 digits."
    return f"The CPF number: [{user_input}] is valid!"


cpf = input("Type the CPF number: ").strip()

print(formated_response(cpf))
