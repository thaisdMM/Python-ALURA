# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.


class Client:
    def __init__(self, name: str, age: int, city: str, phone: str):
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone

    def __str__(self):
        return f"Client: {self.name}, age: {self.age}, city: {self.city}, phone: {self.phone}"


leonardo = Client("Leonardo Siqueira", 33, "Juatuba", "9999-9999")
lindalva = Client("Lindalva Souza", 55, "Sorocaba", "8888-8888")
mario = Client("Mario Santos", 27, "Santos", "7777-7777")

print(leonardo)
print(lindalva)
print(mario)
