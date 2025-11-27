def recursive_sum(number: int) -> int:
    # 1. BASE CASE: The stop condition.
    # The sum of 1 up to 1 is simply 1.
    # This value starts the unwinding/calculation phase.
    if number == 1:
        return 1

    # 2. RECURSIVE STEP: The function calls itself with a smaller input (number - 1).
    # The current 'number' is ADDED to the result of the previous, smaller sum.
    # The calculation (the addition) is DEFERRED until the recursive call returns a value.
    return number + recursive_sum(number - 1)


user_input = int(input("Type a number: "))

print(f"The sum of 1 to {user_input} = {recursive_sum(user_input)}")
