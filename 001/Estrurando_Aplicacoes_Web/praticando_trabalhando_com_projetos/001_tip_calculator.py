def clear_input(user_input):
    try:
        number = abs(float(user_input))
        return number
    except (ValueError, TypeError):
        return None


def tip_calculator(bill_amount: float, tip_value: float) -> float:
    return bill_amount * (tip_value / 100)


def total_to_pay(bill: float, tip: float):
    return bill + tip


def validate_input(bill, tip):
    is_bill_a_number = clear_input(bill)
    if not is_bill_a_number:
        return (None, None)
    is_tip_a_number = clear_input(tip)
    if not is_tip_a_number:
        return (None, None)
    else:
        return (is_bill_a_number, is_tip_a_number)


def show_bill_with_tip(bill_amount, tip_value):
    validation_result = validate_input(bill_amount, tip_value)
    if validation_result == (None, None):
        print("Error: bill amount and tip value must be a value number: ")
    else:
        bill, tip = validation_result
        total_tip = tip_calculator(bill, tip)
        total_bill = total_to_pay(bill, total_tip)
        print(f"\nTip value: U${total_tip:.2f}")
        print(f"Total bill amount: {total_bill:.2f}")


bill = input("Type the bill amount: ")
tip = input("Type the tip value: ")


if __name__ == "__main__":
    show_bill_with_tip(bill, tip)
