from modelos.carros import Carros

carro_1 = Carros ('corolla', 'toyota', 'Vermelho', '112', 'R$ 99.999,00')

carro_2 = Carros ('Civic', 'Honda', 'Preto', '105', 'R$ 89.999,00')

carro_3 = Carros ('Sentra', 'Nissan', 'Branco', '97', 'R$ 79.999,00')

carro_2.alternar_estado()

def main():
    Carros.listar_carros()

if __name__ == '__main__':
    main()