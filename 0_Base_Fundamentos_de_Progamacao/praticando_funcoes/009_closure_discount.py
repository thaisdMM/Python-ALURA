def create_discount_applier(percentage_discount: float):
    # This outer function acts as a 'factory' that specializes a reusable
    # discount function (the closure) with a fixed percentage_discount.
    def calculate_final_price(price: float):
        return price - (price * (percentage_discount / 100))

    return calculate_final_price


discount_percentage = float(input("Type the discount percentage: "))
purchase_value = float(input("Type the purchase value: "))

# Factory: Call to the outer function (the factory) fixes the percentage,
# creating a specialized function (the closure) instance.
discount_applier = create_discount_applier(discount_percentage)


print(f"The final price with discount: U$ {discount_applier(purchase_value)}")
