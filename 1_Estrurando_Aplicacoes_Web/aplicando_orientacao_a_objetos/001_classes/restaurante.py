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

# # 1- 

# print(restaurantes)
# # local da memoria onde está armazenado o objeto
# # output: [<__main__.Restaurante object at 0x100eb1be0>, <__main__.Restaurante object at 0x100e5b250>]

# # 2-
# print(restaurante_praca) # output: <__main__.Restaurante object at 0x104295be0>

# # 3- dir - lista várias informações - atriutos, métodos
# # -> bom para olhar quando existe uma classe que a gente não conhece
# print(dir(restaurante_praca))

# 4- vars - dicionário dos atributos e metodos
print(vars(restaurante_praca)) 
# output: {'nome': 'Praça', 'categoria': 'Gourmet'} - não apareceu o ativo

