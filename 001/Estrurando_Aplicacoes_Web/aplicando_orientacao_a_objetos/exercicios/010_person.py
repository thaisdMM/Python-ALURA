# 1- Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# 2- Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# 3- Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# 4- Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.


class Person:
    """
    Defines a new person with name (str), age (int) and profession (str).”.
    """

    def __init__(self, name: str = "", age: int = 0, profession: str = ""):
        self.name = name
        self.age = age
        self.profession = profession

    def __str__(self):
        return f"Name: {self.name:<15} | Age: {self.age:<5} | Profession: {self.profession:<20}"

    def birthday(self):
        self.age += 1

    @property
    def greeting(self):
        if self.profession:
            return f"Hello, my name is {self.name}, I work as a {self.profession}. Nice to meet you!"
        return f"Hello, my name is {self.name}, it's a pleasure to meet you."


def linha():
    return "=-" * 30


maria = Person("Maria Santana", 36, "Doctor")
lucas = Person("Lucas Moura", 15)
geovana = Person("Geovana Mata", 33, "Detective")


# __str__ method
print("Implementing __str__ method")
print()
print(maria)
print(lucas)
print(geovana)
print(linha())

# changing Maria's profession, property updates automatically
print()
print(maria.greeting)
maria.profession = "Hospital Manager"
print(
    f"\nUpdating [{maria.name}] profession, and the greeting @property updates automatically:\n"
)
print(maria.greeting)
print(linha())

# Updating Ages
lucas.birthday()
geovana.birthday()
print()
print("Implementing __str__ method, after Birthday\n")
print(maria)
print(lucas)
print(geovana)
print(linha())

# Personalized Greetings
print()
print("Personalized Greetings\n")
print(maria.greeting)
print(lucas.greeting)
print(geovana.greeting)
print(linha())
