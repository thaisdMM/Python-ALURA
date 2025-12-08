from modelos.avaliacao import Avaliacao


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
        # 8- criou uma classe avalicao em modelos e agora adicionou no construtor avaliacao
        self._avaliacao = []
        # 7 - pegou a classe, fez um append na lista de restaurante do proprio restaurante(self) que vai ser criado
        Restaurante.restaurantes.append(self)

    # método exibe string
    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    # Vai adicionar o @classmethod para dizer que é um método da classe
    # não precisa de instanciar a classe para acessar esses métodos
    @classmethod
    def listar_restaurantes(cls):
        # colocou entre chaves para manter a formatação :<25
        print(
            f"{'Nome do restaurante':<25} | {'Categoria':<25} | {'Avaliação':<25} | {'Status'}"
        )
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante._nome:<25} | {restaurante._categoria:<25} | {restaurante.media_avaliacoes:<25} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

    # 9- criou metodo receber avaliacao
    def receber_avalicao(self, cliente, nota):
        # objeto da classe Avalicao

        # 12- fazendo uma pequena validação na nota que nao existia
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # 10- fez o metodo e depois transformou em property para ser capaz de ler esse metodo
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            # 11- removeu o valor 0 de quando não tem avaliação e colocou -
            return "-"
        # ternário - pega todas as notas de _avalicao e soma todas as notas
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        # usou o round para arrendondar e pegar só uma casa com 1
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
