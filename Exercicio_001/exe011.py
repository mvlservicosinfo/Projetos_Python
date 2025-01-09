n = float(input('Informe a nota: '))
if n >= 60:
    print('Aprovado')
else:
    if n >= 40:
        print('Reavaliação')
    else:
        print('Reprovado')
print('Boas férias')