# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.


class Restaurant:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.active = False

    def __str__(self):
        return f"Restaurant: {self.name} | Category: {self.category}"


italianinho = Restaurant(name="Italianinho", category="Italian Food")

# before __str__
print(italianinho.name)
print(italianinho.category)

# after method __str__
print(italianinho)
