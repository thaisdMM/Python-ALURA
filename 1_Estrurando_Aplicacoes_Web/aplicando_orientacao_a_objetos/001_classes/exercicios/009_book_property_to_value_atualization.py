class Livro_Comparacao:
    def __init__(self, titulo="", autor="", paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

        # Atributo Estático (Calculado UMA VEZ no construtor)
        # O valor é salvo no objeto. Se self.titulo mudar, este valor ficará obsoleto.
        self.titulo_autor_estatico = f"{self.titulo} por {self.autor}"

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

    # Propriedade Dinâmica (A forma mais recomendada para cálculos leves)
    @property
    def titulo_autor_property(self):
        # O CÁLCULO é executado TODA VEZ que a propriedade é acessada.
        # Ele sempre retorna o valor mais atualizado de self.titulo e self.autor.
        # A sintaxe de acesso é: livro.titulo_autor_property (SEM PARÊNTESES)
        return f"{self.titulo} por {self.autor}"

    # Método Dinâmico (Comportamento semelhante ao @property, mas sintaxe diferente)
    def titulo_autor_metodo(self):
        # O CÁLCULO também é executado TODA VEZ que o método é chamado.
        # Ele também retorna o valor mais atualizado.
        # A sintaxe de acesso é: livro.titulo_autor_metodo() (COM PARÊNTESES)
        return f"{self.titulo} por {self.autor}"

    # Método de Recálculo Manual (O que seria necessário para o Atributo Estático)
    def forcar_atualizacao(self):
        # Se usássemos apenas o Atributo Estático, precisaríamos criar e chamar
        # um método manualmente para corrigir o valor após uma alteração.
        print("--- Recálculo Manual Forçado ---")
        self.titulo_autor_estatico = f"{self.titulo} por {self.autor}"


# ----------------------------------------------------------------------

livro = Livro_Comparacao("Duna", "Frank Herbert", 800)

print(f"1. Estático Inicial: {livro.titulo_autor_estatico}")
print(f"2. Property Inicial: {livro.titulo_autor_property}")
print("-" * 30)

# Altera a base
livro.titulo = "Duna - Clássico"

# COMPARAÇÃO APÓS ALTERAÇÃO:
print(f"Estático Obsoleto: {livro.titulo_autor_estatico}")  # Mantém 'Duna'
print(
    f"Property Atualizado: {livro.titulo_autor_property}"
)  # Retorna 'Duna - Clássico'
print(f"Método Atualizado: {livro.titulo_autor_metodo()}")  # Retorna 'Duna - Clássico'

# Se tivéssemos que corrigir o valor estático, teríamos que chamar o método:
livro.forcar_atualizacao()
print(f"Estático Corrigido: {livro.titulo_autor_estatico}")
