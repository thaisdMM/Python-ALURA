class Restaurant:
    name = ""
    category = ""
    active = False


def restaurant_active(restaurant):
    if not restaurant.active:
        return f"The Restaurant {restaurant.name} is not active."
    return f"The Restaurant {restaurant.name} is active."


restaurante_praca = Restaurant()
restaurante_praca.name = "Praça"
restaurante_praca.category = "Gourmet"

restaurante_pizza = Restaurant()
restaurante_pizza.name = "Pizza Place"
restaurante_pizza.category = "Fast Food"


restaurante_praca.category = "Italian"
print(f"Restaurant: {restaurante_praca.name}")
print(restaurant_active(restaurante_praca))
category = restaurante_praca.category
print(f"Restaurant {restaurante_praca.name} | Category: {category}")

restaurante_praca.name = "Bistro"
print(f"Restaurant {restaurante_praca.name} | Category: {restaurante_praca.category}")

if restaurante_pizza.category == "Fast Food":
    print(f"The Restaurant: {restaurante_pizza.name} category is Fast Food!!!")
else:
    print(f"The Restaurant: {restaurante_pizza.name} category is NOT Fast Food.")


restaurante_pizza.active = True
print(restaurant_active(restaurante_pizza))

print(f"\nRestaurant {restaurante_praca.name} | Category: {category}")
