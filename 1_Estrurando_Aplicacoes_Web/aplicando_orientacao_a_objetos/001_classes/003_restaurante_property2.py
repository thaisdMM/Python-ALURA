class Restaurante:
    # 7 - atributo de classe
    restaurantes = []

    # construtor - chamado automaticamente quando a classe é instanciada
    # self é convenção - representa a instância da própria classe
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        # atributo protegido
        self._ativo = False
        # 7 - pegou a classe, fez um append na lista de restaurante do proprio restaurante(self) que vai ser criado
        Restaurante.restaurantes.append(self)

    # método exibe string
    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    # não usa o self, pois esta selecionando da lista que já armazenou esse objeto
    def listar_restaurantes():
        # colocou entre chaves para manter a formatação :<25
        print(f"{'Nome do restaurante':<25} | {'Categoria':<25} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante._nome:<25} | {restaurante._categoria:<25} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"


# instanciândo um objeto
restaurante_praca = Restaurante("praça", "Gourmet")
resturante_pizza = Restaurante("pizza express", "Italiano")


# # erro ao mudar o ativo sem setter definido:
# restaurante_praca.ativo = True
# #output: AttributeError: property 'ativo' of 'Restaurante' object has no setter

## Convenção:
# # não mudar atribito protegido diretament como em:
# restaurante_praca._nome = "praça 2.0"

Restaurante.listar_restaurantes()
