class Listar_Dicionario():

    def __init__(self, valor):
        self.valor = valor

    def calculo(self):
        dict_mercado = {'Batata': 9.00, 'laranja': 18.00, 'Uva': 100.00}
        dict_valor = {t: (lambda m: self.valor - m if m < self.valor else 'Acabou o dinheiro')(m) for (t, m) in dict_mercado.items()}
        print(dict_valor)

