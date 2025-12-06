class Restaurante:
    nome = ""
    categoria = ""
    ativo = False


# instanciândo um objeto
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
resturante_pizza = Restaurante()

restaurantes = [restaurante_praca, resturante_pizza]

# 1-

print(restaurantes)
# local da memoria onde está armazenado o objeto
# output: [<__main__.Restaurante object at 0x100eb1be0>, <__main__.Restaurante object at 0x100e5b250>]

# 2-
print(restaurante_praca)  # output: <__main__.Restaurante object at 0x104295be0>

# 3- dir - lista várias informações - atriutos, métodos
# -> bom para olhar quando existe uma classe que a gente não conhece
print(dir(restaurante_praca))

# 4- vars - dicionário dos atributos e metodos
print(vars(restaurante_praca))
# output: {'nome': 'Praça', 'categoria': 'Gourmet'} - não apareceu o ativo

# 5- construtor


class Restaurante:
    # construtor
    # self é convenção
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # método exibe string
    def __str__(self):
        return f"{self.nome} | {self.categoria}"


# instanciândo um objeto
restaurante_praca = Restaurante("Praça", "Gourmet")
resturante_pizza = Restaurante("Pizza Express", "Italiano")

# # nesse print o output é o objeto
print(restaurante_praca)  # output: <__main__.Restaurante object at 0x100badbe0>
print(resturante_pizza)  # output: <__main__.Restaurante object at 0x100b57250>

# com o vars() nesse print o output já é o dicionáio
print(vars(restaurante_praca))
# output: {'nome': 'Praça', 'categoria': 'Gourmet', 'ativo': False}
print(vars(resturante_pizza))
# # output: {'nome': 'Pizza Express', 'categoria': 'Italiano', 'ativo': False}

# 6- criar um método __str__ , nem precisa chamar já exibe:
print(restaurante_praca)  # output: Praça | Gourmet
print(resturante_pizza)  # output: Pizza Express | Italiano

# 7 - criando métodos próprios


class Restaurante:
    # 7 - atributo de classe
    restaurantes = []

    # construtor - chamado automaticamente quando a classe é instanciada
    # self é convenção - representa a instância da própria classe
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        # 7 - pegou a classe, fez um append na lista de restaurante do proprio restaurante(self) que vai ser criado
        Restaurante.restaurantes.append(self)

    # método exibe string
    def __str__(self):
        return f"{self.nome} | {self.categoria}"

    # não usa o self, pois esta selecionando da lista que já armazenou esse objeto
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")


# instanciândo um objeto
restaurante_praca = Restaurante("Praça", "Gourmet")
resturante_pizza = Restaurante("Pizza Express", "Italiano")

Restaurante.listar_restaurantes()
