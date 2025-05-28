from modelos.avaliacao import Avaliacao

class Carros:
    carros = []

    def __init__(self, nome, marca, cor, cavalos, valor):
        self.nome = nome.title()
        self.marca = marca.upper() 
        self.cor = cor
        self.cavalos = cavalos
        self.valor = valor
        self._ativo = False
        self._avaliacao = []
        Carros.carros.append(self)

    @classmethod
    def listar_carros(cls):
        print(f"{'Nome do carro'.ljust(15)} | {'Marca'.ljust(15)} | {'Cor'.ljust(15)} | {'Cavalos'.ljust(15)} | {'Valor'.ljust(15)} | {'Avaliação'.ljust(15)} | {'Status'}")
        print('-'*130)
        for carro in cls.carros:
            print(carro)

    @property 
    def ativo(self):
        return 'Vendido' if self._ativo else 'Não Vendido'

    def __str__(self):
        return f"{self.nome.ljust(15)} | {self.marca.ljust(15)} | {self.cor.ljust(15)} | {str(self.cavalos).ljust(15)} | {str(self.valor).ljust(15)}| {str(self.media_avaliacoes).ljust(15)} | {self.ativo}"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota_carro ):
        if 0 < nota_carro <= 10:
            avaliacao = Avaliacao(cliente, nota_carro)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota_carro for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media