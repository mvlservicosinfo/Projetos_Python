class Lista():

    def __init__(self):
        pass

    calc = [x for x in range(10)]

    dict_mercado = {'laranja':18.00,'Batata':9.40, 'Mamao':5.00}
    dict_economia ={k:('Tá Barato' if c <18.00 else 'Tá Caro') for (k,c) in dict_mercado.items()}

