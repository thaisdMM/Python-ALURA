products = input(
    "Type the products separated by commas, for example 'apple,banana': "
).split(",")
# print(products)

price = input("Type the price separeted by commas, for example: '2.5,1.8': ").split(",")
# print(price)
converted_price = [float(value) for value in price]
# print(converted_price)

products_price_dict = dict(zip(products, converted_price))
# print(products_price_dict)
for key, value in products_price_dict.items():
    print(f"{key.strip()}: U${value:.2f}")
