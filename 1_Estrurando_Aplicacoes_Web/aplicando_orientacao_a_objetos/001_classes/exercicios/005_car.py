# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.


class Car:
    def __init__(self, model: str, color: str, year: int):
        self.model = model
        self.color = color
        self.year = year

    def __str__(self):
        return f"Model: {self.model} | color: {self.color} | year {self.year}"


corsa = Car("Corsa", "read", 2009)
print(corsa)
