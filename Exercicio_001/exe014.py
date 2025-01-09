soma = 0
try:
    for cont in range(10):
        n = float(input('Informe um número: '))
        soma += n
        print(soma)
except (ValueError, TypeError) as erro:
    print(f'Erro: {erro}')