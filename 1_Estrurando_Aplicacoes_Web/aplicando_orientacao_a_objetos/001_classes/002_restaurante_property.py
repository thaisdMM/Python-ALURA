class Restaurante:
    # 7 - atributo de classe
    restaurantes = []

    # construtor - chamado automaticamente quando a classe é instanciada
    # self é convenção - representa a instância da própria classe
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        # atributo protegido
        self._ativo = False
        # 7 - pegou a classe, fez um append na lista de restaurante do proprio restaurante(self) que vai ser criado
        Restaurante.restaurantes.append(self)

    # método exibe string
    def __str__(self):
        return f"{self.nome} | {self.categoria}"

    # não usa o self, pois esta selecionando da lista que já armazenou esse objeto
    def listar_restaurantes():
        # colocou entre chaves para manter a formatação :<25
        print(f"{'Nome do restaurante':<25} | {'Categoria':<25} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante.nome:<25} | {restaurante.categoria:<25} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"


# instanciândo um objeto
restaurante_praca = Restaurante("Praça", "Gourmet")
resturante_pizza = Restaurante("Pizza Express", "Italiano")

Restaurante.listar_restaurantes()

# erro sem ativo ser protegido antes: AttributeError: property 'ativo' of 'Restaurante' object has no setter
