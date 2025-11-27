def convert_string_to_integers(phone_list: list):
    try:
        return [int(phone) for phone in phone_list]
    except ValueError:
        # Using `None` in the except block ensures a consistent return type.
        # instead of mixing types (like returning a string), which helps maintain predictable behavior.
        return None


def is_type_int(converted_list: list):
    if not converted_list:
        return False
    for phone in converted_list:
        if not isinstance(phone, int):
            return False
        return True


def formated_response(phones: list):
    converted_phone_list = convert_string_to_integers(phones)
    is_int = is_type_int(converted_phone_list)
    if is_int:
        return "All numbers were conveted correctly!"

    return "Error: list were not converted correctly, because there were not only integer values."


phones = ["11987654321", "21912345678", "31987654321", "11911223344"]
phones2 = ["abc222999", "21912345678", "31987654321", "11911223344"]

print(formated_response(phones))
print(formated_response(phones2))
