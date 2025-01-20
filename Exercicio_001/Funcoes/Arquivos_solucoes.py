class Arquivos():

    def __init__(self, txt):
        self.txt = txt
        arq2 = open("/home/marcello/Documentos/Teste.txt","w")
        arq2.write(self.txt)
        arq2.close()
        arq3 = open("/home/marcello/Documentos/Teste.txt","r")
        print(arq3.read())
        arq3.close()
        arq4 = open("/home/marcello/Documentos/Teste.txt","a")
        arq4.write(txt)
        arq4.close()