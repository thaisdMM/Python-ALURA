# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.


class Restaurant:
    def __init__(self, name: str, category: str, stars: int, city: str, active=False):
        self.name = name
        self.category = category
        self.stars = stars
        self.city = city
        self.active = active


fazendinha = Restaurant(
    name="Fazendinha",
    category="Comida Mineira",
    stars=4,
    city="Serra do Cipó",
    active=True,
)
print(fazendinha.name)
print(fazendinha.city)
print(fazendinha.active)
