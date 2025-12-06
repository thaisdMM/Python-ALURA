from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")

# 1- trabalhar com avalicao de apenas 1 restaurnte
# restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
# restaurante_japones = Restaurante("Japa", "Japonesa")
# restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avalicao("Gui", 10)
restaurante_praca.receber_avalicao("Lais", 8)
restaurante_praca.receber_avalicao("Emy", 5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
