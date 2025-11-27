def total_sales(values: int):
    return sum(values)


def converted_to_numbers(sales_value: str):
    separated = sales_value.split()

    # Converts each text element into a float using a list comprehension
    converted_numbers = [float(value) for value in separated]

    return converted_numbers


def formated_response(sales_values):
    values_converted = converted_to_numbers(sales_values)
    total = total_sales(values_converted)
    print(f"The total sales were: U${total:.2f}")


sales_values = input("Type the sales values: U$")
formated_response(sales_values)

# Pythonic solution

# Reads the user's input and immediately splits the line into a list of strings
sales_values = input("\nType the sales values: U$").split()

# Converts each string to float using map() and calculates the total with sum()
# - map(float, sales_values) applies float() to each element lazily
# - sum(...) consumes the iterator and produces the final numeric total
total = sum(map(float, sales_values))

# Prints the formatted response with two decimal places
print(f"The total sales were: U${total:.2f}")
