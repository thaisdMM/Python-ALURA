map_operation = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: division by zero.",
}


def lambda_calculator(number1: float, number2: float, operation: str):
    operationt_selected = map_operation[operation]
    result = operationt_selected(number1, number2)
    return result


def operation_exibition():

    while True:
        print("-=" * 10)
        print("CALCULATOR")
        print("-=" * 10)

        finish_program = False

        try:
            number1 = float(input("\nType the first number: "))
            number2 = float(input("\nTyepe the second number: "))
            operation = input("\nChoose the operation (| + | - | * | / |): ").strip()
            if operation not in map_operation.keys():
                print("Ivalid operator, try again.")
                continue
            result = lambda_calculator(number1, number2, operation)
            print(f"\n The result is: {result}")

        except (ValueError, KeyError):
            print("ERROR: Invalid input for number or operation.")

        while True:
            leave = (
                input("\nDo you want to exit the program? Answer: [Y] or [N]: ")
                .upper()
                .strip()[0]
            )
            if leave == "Y":
                finish_program = True
                break
            elif leave == "N":
                break
            else:
                print("\nIncorrect answer. Answer Y or N:")
        if finish_program == True:
            break

    print("\nProgram finished.")


if __name__ == "__main__":
    operation_exibition()
