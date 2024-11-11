from Exercicio_001.Funcoes.Exercicio001 import Execicio1
from Exercicio_001.Funcoes.Exercicio_002 import Exercicio_2
from Exercicio_001.Funcoes.Fatorial import Fatorial
from Exercicio_001.Funcoes.Perimetro_Retangulo import Perimetro
from Exercicio_001.Funcoes.Saudacao_Msg import SaudacaoMsg
from Exercicio_001.Funcoes.saudacao import saudacao

if __name__ == '__main__':
    t = Execicio1(5)
    t.executar()
    print("")
    s=Exercicio_2(2,8)
    print(s.Area())

    valor = int(input("Digite um valor: "))
    f=Fatorial(valor)
    print(f'O fartorial de {valor} é {f.fatorial()}')

    w = saudacao("Marcello")
    print(w.saudacao())

    h = SaudacaoMsg('Marcello!','Tenha um bom dia!')
    print(h.saudacaoMsg())

    y=Perimetro(5,9)
    print(y.calcula_perimetro())






